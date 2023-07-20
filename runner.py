import os
import numpy as np
import time
import multiprocessing as mp


def integrate_sim(dir_path, trial_num_dec, omega, theta, triax):

    start = time.time()
    print(f"Trial {trial_num_dec} initiated",flush=True)

    TO_RAD_YEAR=24.8364706645 # synchronous rotation in rad/year

    omg_in = str(omega*TO_RAD_YEAR)
    tht_in = str(theta)
    trx_in = str(triax)

    # make copy of input directory
    os.system("cp -r ./se_res/dir_template ./se_res/trial_"+str(trial_num_dec))

    # edit copy of input file
    file="./se_res/trial_"+str(trial_num_dec)+"/init_system.json"
    os.system("sed -i '' \"s/omega/"+omg_in+"/\" "+file)
    os.system("sed -i '' \"s/theta/"+tht_in+"/\" "+file)
    os.system("sed -i '' \"s/triax/"+trx_in+"/\" "+file)

    # run simulation
    os.system("./bin/simulate ./se_res/trial_"+str(trial_num_dec))

    # extract data

    data = np.loadtxt('/Users/henryyuan/Documents/Github/GRIT_sims/se_res/trial_'+str(trial_num_dec)+'/data_in_mat/Planet', skiprows=1).T
    # t, rx, ry, rz, vx, vy, vz, ax, ay, az, sx, sy, sz, axt = dat
    # omegas = np.sqrt(sx**2 + sy**2 + sz**2)
    # year = 0.4**(3/2)

    file_path = os.path.join(dir_path,"trial_"+str(trial_num_dec)+".npy")
    
    with open(file_path, 'wb') as f:
        np.save(f, data)

    # delete directory
    os.system("rm -rf ./se_res/trial_"+str(trial_num_dec))

    int_time = time.time() - start
    hrs = int_time // 3600
    mins = (int_time % 3600) // 60
    secs = int((int_time % 3600) % 60)
    print(f"Trial {trial_num_dec} completed in {hrs} hours {mins} minutes {secs} seconds.", flush=True) 

def run_sim(trial_num, n_trials=50):

    # max_omega = 4. # 2 because otherwise obliquity is excited # (1+(np.pi/2/np.arctan(1/Q_tide)))
    # omega_to_n = max_omega*np.random.default_rng().uniform()
    omegas = [1.6,3.1]
    omega_to_n = omegas[trial_num % len(omegas)]
    thetas = np.radians(np.linspace(0,180,int(n_trials / len(omegas))))
    theta = thetas[trial_num//2]
    base_moment = 2.89068735e-14

    # make output directory and file
    dir_path = "./se_res/data/2body_data"
    if trial_num == 0:
        if os.path.exists(dir_path):
            print("Error: Directory already exists")
            exit()
        os.mkdir(dir_path)
    else:
        while (not os.path.exists(dir_path)):
            time.sleep(1)

    ### RUN SIMULATION ###
    triax = 1.00001*base_moment
    integrate_sim(dir_path,trial_num,omega_to_n,theta,triax)

    ### Re-RUN SIMULATION with same parameters, except just j2 ###
    trial_num_2 = trial_num + 0.1
    triax = base_moment
    integrate_sim(dir_path,trial_num_2,omega_to_n,theta,triax)

# main function
if __name__ == '__main__':
    # to change params, see keyword args in run_sim()
    n_trials = 50 # if I change this, make sure to also change in keyword args in run_sim()
    start = time.time()
    with mp.Pool(processes=n_trials) as pool:
        pool.map(run_sim, range(n_trials))
    
    tot_time = time.time() - start
    hrs = tot_time // 3600
    mins = (tot_time % 3600) // 60
    secs = int((tot_time % 3600) % 60)
    print(f"Total Runtime: {hrs} hours {mins} minutes {secs} seconds", flush=True)

