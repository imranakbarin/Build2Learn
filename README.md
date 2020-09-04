# BuildNLearn
BuildNLearn Community

## Getting Started
Install git locally to clone the project, alternatively you can download directly from above without installing git. 

To clone via git use below command from your command prompt:

```
git clone https://github.com/imranakbarin/Build2Learn.git
```

Change into the directory you downloaded:

```
cd Build2Learn
```

Create virtual environment

```
py -m venv build2learn-env
```

Run the below command, as some windows user face running scripts

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Activate the virtual environment 

```
.\build2learn-env\Scripts\activate
```

### Install requirement.txt

```
pip install -r requirements.txt
```

### Run the project

```
flask run
```

### API Available for Chennai Covid-19 Cases, that can be consumed from below end points

### Chennai Covid-19 Zone-wise Timeseries(Updated Everyday)

```
http://www.buildnlearn.in/api/chennaizones/cases
```

### Chennai Street-Wise Report(Everyday or based on the updates from Chennai Corporation)

```
http://www.buildnlearn.in/api/chennaiStreet/daily

```


For News API to work, get api key from https://newsapi.org/ 

### If you are willing to contribute, we would love it!

### Thanks to Covid19 India for APIs https://api.covid19india.org/

#### Thank you :)
