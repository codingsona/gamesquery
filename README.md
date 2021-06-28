# Game Search Service

A simple django service http://www.giantbob.com/api/search API.

- Technology Stack: Python, Django Rest Framework, Docker
- Default Filters: "limit=5, page=0, offset=0"
- Default Fields: "id, name, date_added, api_detail_url, number_of_user_reviews"

## Features
Use below examples to search and filter a game:
- Search for a game using:  
  GET /v1/games/{game_name}
- Add Filters on the result:  
  GET /v1/games/{game_name}?limit={resultsPerPage}&page={pageIndex}&format=json
- Select Fields to retrieve:
  GET /v1/games/{game_name}?fields=field1,field2,field3

## Setup
1. Clone the repository
2. Get API key from www.giantbomb.com/api
3. Start the docker service and then issue the below command:
   docker-compose up --build


## Examples (use curl or browser)
- http://127.0.0.1:8000/v1/games/poke
- http://127.0.0.1:8000/v1/games/poke?limit=2&page=2
- http://127.0.0.1:8000/v1/games/poke?limit=2&page=2&fields=id,aliases,description

![image](https://user-images.githubusercontent.com/59982549/123673093-ec37bd00-d7f4-11eb-969a-25d33cbbd95e.png)



