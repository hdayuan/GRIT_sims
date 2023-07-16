run:
	./bin/simulate sample/se_res
plot:
	python3 ./sample/se_res/plot.py
clean:
	rm -f ./sample/se_res/init_system_posvel.json
	rm -f ./sample/se_res/data_tmp.json
	rm -f ./sample/se_res/current_system.json
	rm -rf ./sample/se_res/data_in_mat

runt:
	./bin/simulate sample/sun_earth_moon
plott:
	python3 ./sample/sun_earth_moon/plot.py
cleant:
	rm -f ./sample/sun_earth_moon/init_system_posvel.json
	rm -f ./sample/sun_earth_moon/data_tmp.json
	rm -f ./sample/sun_earth_moon/current_system.json
	rm -rf ./sample/sun_earth_moon/data_in_mat