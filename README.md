# Game Search Service

A simple django web service to search for games. The service can be accessed by curl or browser. The service renders the result in json, browsable api and admin formats. An example service has been deployed to AWS and can be accessed via http://34.220.37.66:8000/v1/games?query={game_query}. Replace {game_query} with a query of your choice. The AWS service is available only temporarily. Please follow the Setup steps to set your own service. It utilizes http://www.giantbob.com/api/search API as backend.

- Technology Stack: Python, Django Rest Framework, Docker
- Default Filters: "limit=5, page=0, offset=0"
- Default Fields: "id, name, date_added, api_detail_url, number_of_user_reviews"

## Features
Use below end point to search and filter a game query:
- Search for a game using:  
  GET /v1/games?query={game_query}
- Add Filters on the result:  
  GET /v1/games?query={game_query}?limit={resultsPerPage}&page={pageIndex}&format=json
- Select Fields to retrieve:
  GET /v1/games?query={game_query}?fields=field1,field2,field3
- Choose the format of output
- GET /v1/games?query={game_query}?format=json

## Setup
1. Clone the repository  
   git clone https://github.com/codingsona/gamesquery.git  
2. Get API key from www.giantbomb.com/api and configure .env file under project root directory gamesquery.   
   contents of .env file:
   GIANTBOMB_API_KEY='YOUR_API_KEY'  
3. To start manually, use steps 4 and 5. To start via docker, use step 6.
4. Create a new python virtual environment. Activate the virtual env and install the required python modules manually:  
   python -m venv myvenv  
   source myenv/bin/activate  
   pip install -r requirements.txt  
5. Execute below commands to start the application:  
   python manage.py runserver 0.0.0.0:8000  
6. Start the docker service and then issue the below command:  
   docker-compose up --build


## Examples (use curl or browser)
- http://34.220.37.66:8000/v1/games?query=poke
- http://34.220.37.66:8000/v1/games?query=poke?limit=2&page=2
- http://34.220.37.66:8000/v1/games?query=poke?limit=2&page=2&fields=id,aliases,description

![image](https://user-images.githubusercontent.com/59982549/123736563-2d13ee00-d856-11eb-8886-88bd9a256ca3.png)



