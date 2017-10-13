## Introduction
python flask app which perform nmap port scanning on the host: 'vulnweb.com'

Disclaimer: Network probing or port scanning tools are only permitted when used in conjunction with a residential home network, or if explicitly authorised by the destination host and/or network.

## Developers Guide
OS:   
`macOS Sierra 10.12.6`
  
Development tools:  
`Python 3.6.1`  
`flask 0.12.2`  
`vuejs 2.9.1`  
`nmap 7.6`
  
Deployment tools:  
`Docker 17.09.0`

Hosting Services:  
Frontend: `AWS S3 webhosting`  
Backend: `AWS ECS`

## Getting Started
### Configuration

#### Setup AWS config  
Install awscli http://docs.aws.amazon.com/cli/latest/userguide/installing.html  
```bash
$ pip install awscli --upgrade --user
```

or use homebrew  
```bash
$ brew install awscli
```

make sure awscli is installed  
```bash
$ aws --version
```

configure aws credentials http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html  
```bash
$ aws configure  
AWS Access Key ID [None]: [YOUR_ACCESS_KEY]  
AWS Secret Access Key [None]: [YOUR_SECRET_KEY]  
Default region name [None]: [YOUR_REGION]  
Default output format [None]: json  
```

### Start vuejs frontend
```bash
$ cd scanner-ui
```  
```bash
$ npm install
```  
```bash
$ npm run start
```  

The app will run at http://localhost:8080/

### Start dockerise flask backend  

Change directory  
```bash
$ cd scanner-api
```  
build docker image  
```bash
$ docker build -t port-scanner:latest .
```  
start docker container  
```bash
$ docker run -p 5000:80 port-scanner 
```  

The app will run at http://localhost:5000/

### Deploy to AWS
#### Frontend Deploy to AWS S3  
create a bucket `nmap-scanner` in aws s3  

Change directory  
```bash
$ cd scanner-ui
```  
build the `dist` files  
```bash
$ npm run build
```  
deploy to aws s3   
```bash
$ npm run deploy
```  

#### Backend Deploy to AWS ECS
Change directory  
```bash
$ cd scanner-api
```  

Push docker image to AWS ECR http://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html  
1. Retrieve the docker login command  
```
aws ecr get-login --no-include-email --region ap-southeast-1
```
2. Run the docker login command that was returned in the previous step.  
3. Build your docker image  
```
docker build -t port-scanner .
```  
4. Tag your docker image  
```
docker tag port-scanner:latest [your_docker_image_repository_url:latest]
```
5. Push your image  
```
docker push [your_docker_image_repository_url:latest]
```

Update task and service in AWS ECS
