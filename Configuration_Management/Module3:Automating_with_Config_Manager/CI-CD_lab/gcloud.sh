gcloud auth list #To list the active account name 
gcloud config list project #List the peoject id
export PROJECT_ID=$(gcloud config get-value project)  # to set the project ID
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)') #to set the PROJECT_NUMBER
export REGION=us-east1 #To set the region
gcloud config set compute/region $REGION 
#To enable the APIs: 
gcloud services enable container.googleapis.com \
    cloudbuild.googleapis.com \
    sourcerepo.googleapis.com \
    containeranalysis.googleapis.com
#to create an Artifactory Registry Docker repo
gcloud artifacts repositories create my-repository \
  --repository-format=docker \
  --location=$REGION
gcloud container clusters create hello-cloudbuild --num-nodes 1 --region $REGION #to create a K8s cluster to deploy the sample application of this lab
git config --global user.email "you@example.com" #COnfiguriong GIT with my own email 
git config --global user.name "Your Name" #Cnfiguring git with my username



#Step2 Create the GIT repositorues in CLoud Source Repositories
gcloud source repos create hello-cloudbuild-app
gcloud source repos create hello-cloudbuild-env
cd ~
mkdir hello-cloudbuild-app
gcloud storage cp -r gs://gwg-content/gic225/gke-gitops-tutorial-cloudbuild/* hello-cloudbuild-app
cd ~/hello-cloudbuild-app #to configure the source reposirories.
export REGION=us-east1
sed -i "s/us-central1/$REGION/g" cloudbuild.yaml
sed -i "s/us-central1/$REGION/g" cloudbuild-delivery.yaml
sed -i "s/us-central1/$REGION/g" cloudbuild-trigger-cd.yaml
sed -i "s/us-central1/$REGION/g" kubernetes.yaml.tpl
PROJECT_ID=$(gcloud config get-value project)
git init
git add .
git remote add google "https://source.developers.google.com/p/${PROJECT_ID}/r/hello-cloudbuild-app"
git commit -m "Initial commit"

#Whit this docker file 
cd ~/hello-cloudbuild-app
COMMIT_ID="$(git rev-parse --short=7 HEAD)"
gcloud builds submit --tag="${REGION}-docker.pkg.dev/${PROJECT_ID}/my-repository/hello-cloudbuild:${COMMIT_ID}" .