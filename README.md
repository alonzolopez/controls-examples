# Setup
This repo contains a variety of example controller implementations.

## Virtual Environment Setup
On Ubuntu:
```bash
python3 -m venv ce-env
source ce-env/bin/activate
```
On Windows:
```bash
python -m venv ce-env
.\ce-env\Scripts\activate
```

### Install Requirements
On Ubuntu:
```bash
pip install -r ./requirements.txt
```
On Windows:
```bash
pip install -r .\requirements.txt
```

You may need to install the following in order to run the plotly plots:
1. Install Node.js and npm following these [instructions](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)
2. Install everything [here](https://github.com/plotly/plotly.py#jupyterlab-support-python-35) under JupyterLab Support
3. (May not need this step) Install all extensions [here](https://github.com/jupyterlab/jupyter-renderers)


## Running
On Ubuntu:
Activate your virtual env if you haven't already done so with
```bash
source ce-env/bin/activate
```
Then launch the jupyter server with
```bash
jupyter notebook
```

On Windows:
Activate your virtual env if you haven't already done so with
```bash
.\ce-env\Scripts\activate
```
Then launch the jupyter server with
```bash
jupyter notebook
```

# Controllers
## Linear Quadratic Regulator
This controller drives the satellite to zero (i.e. crashes into the client). 