run:
	./bin/simulate sample/test
plot:
	python3 plot.py
clean:
	rm -f ./sample/test/init_system_posvel.json
	rm -f ./sample/test/data_tmp.json
	rm -f ./sample/test/current_system.json
	rm -rf ./sample/test/data_in_mat

grid:
	python3 runner.py > output.txt 2> errors.txt

runt:
	./bin/simulate sample/sun_earth_moon
plott:
	python3 ./sample/sun_earth_moon/plot.py
cleant:
	rm -f ./sample/sun_earth_moon/init_system_posvel.json
	rm -f ./sample/sun_earth_moon/data_tmp.json
	rm -f ./sample/sun_earth_moon/current_system.json
	rm -rf ./sample/sun_earth_moon/data_in_mat