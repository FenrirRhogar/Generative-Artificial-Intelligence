all: naive1000 naive500 naiveSphere neural1000 neural500 neuralSphere

naive500:
	python .\naiveReconstruction.py --file data/bunny-500.pts

naive1000:
	python .\naiveReconstruction.py --file data/bunny-1000.pts

naiveSphere:
	python .\naiveReconstruction.py --file data/sphere.pts

neural500:
	python .\neuralNetReconstruction.py --input_pts data/bunny-500.pts
	python .\neuralNetReconstruction.py -e --input_pts data/bunny-500.pts

neural1000:
	python .\neuralNetReconstruction.py --input_pts data/bunny-1000.pts
	python .\neuralNetReconstruction.py -e --input_pts data/bunny-1000.pts

neuralSphere:
	python .\neuralNetReconstruction.py --input_pts data/sphere.pts
	python .\neuralNetReconstruction.py -e --input_pts data/sphere.pts