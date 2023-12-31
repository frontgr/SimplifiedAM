# SimplifiedAM

---

About this project:

- */time* - GET the time difference between a specified local time and the one in Armenia.
- */armenian-cities* - GET cities names with a population data.
- */ararat-info* - GET some information about the Ararat mountain.
- */armenian-dishes* - GET 5 armenian dishes names and their description.
- */random-armenian-word* - GET a random english/armenian word form 90k+ words dictionary.

---

### Technologies used:
1. [Docker](https://docs.docker.com/) and some additional info about [Namespaces](https://www.youtube.com/watch?v=-YnMr1lj4Z8&ab_channel=LiveOverflow) that the [Docker Containers](https://www.youtube.com/watch?v=sHp0Q3rvamk&ab_channel=LiveOverflow) use
2. [Flask](https://flask.palletsprojects.com/en/3.0.x/)

---

## To run the app:
Create docker-network in your working directory:

```yaml
docker network create sam-network
```

Next step is to build the container:

```yaml
docker-compose up --build 
```
Add "-d" after "--build" if you do not want to test the app in debug mode.

To shut down a container:

```yaml
docker-compose down
```
or just do it from Docker GUI.

To run a container again (if you haven't changed any code), use:

```yaml
docker-compose up
```

---
## Additional tools:
For simplicity of sending requests, you can use [Postman](https://learning.postman.com/docs/introduction/overview/) 
