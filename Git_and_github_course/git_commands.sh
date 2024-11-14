git config --global user.email "jcardogo@gmail.com" #configuring the email used for all repositories
git config --global user.name "Alejandro Cardoso" #configuring the name used for all repositories
mkdir ClonedRepos #Creating a directory to contain all git repository directories
cd ClonedRepos/ #Moving to created directory
mkdir HomeLab #Create a new repository local directory
cd HomeLab/ #Moving to created directory
git init #Inilializing a git repository 
ls -l .git/ #Checking the git related content of the new repo
git add disk_usage.py #add a file to stage git 
git status #show some information about the 
'
On branch master

No commits yet

Changes to be committed:       #this section show the current status of the modified files
  (use "git rm --cached <file>..." to unstage)
        new file:   disk_usage.py
'
git commit #save our changes on git, will open a text editor to add a commit message to clarify the action and context
git add  disk_usage.py #this add the modfications to the stage to be commited 
git commit -m 'Add period at the end of error message' #save the changes on our staged files and add the message describing the porpuse of this commit
'
file life cycle on git
1) modified (modified on red): Working tree
2) Staged (modfied on green) : Staging Area
3) Commited (Snapshooted) : Git directory
' 
 git config -l #this command show the configuration on repo
 '
user.email=jcardogo@gmail.com
user.name=Alejandro Cardoso
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
 '

git log #show important informations about commits

'
commit 01655452a0c054e83469e25cbc67ca105729af14 (HEAD -> master)
Author: Alejandro Cardoso <jcardogo@gmail.com>
Date:   Wed Nov 6 10:20:11 2024 -0500

    adding / to the file path to check if it works

commit 6efd3cfbe284ac3f0f0c3715378256bbfb938071
Author: Alejandro Cardoso <jcardogo@gmail.com>
Date:   Wed Nov 6 10:18:51 2024 -0500

    adding the reboot check with check_reboot function

commit e9b27b8c6ab4246f03c168b992aa381e0793dca1
Author: Alejandro Cardoso <jcardogo@gmail.com>
Date:   Wed Nov 6 10:13:08 2024 -0500

    Creating an empty all_checks.py file

commit 68bcc614d96119119e3729bb7579853a48479104
Author: Alejandro Cardoso <jcardogo@gmail.com>
Date:   Wed Nov 6 10:00:12 2024 -0500

    Add period at the end of error message

commit 2d843c6721d806500efc67bf243bd369d01256cb
Author: Alejandro Cardoso <jcardogo@gmail.com>
Date:   Wed Nov 6 09:45:52 2024 -0500

    This is the first commit from git on command liney
'
git diff <file_name> #will show changes on the file

gut commit -a #will shortcut to stage any changes to tracked files and commit them in one step

git log -p #"p" standing for patch showing some details about the changes made on each file

git show 01655452a0c054e83469e25cbc67ca105729af14 #show details of a specific commit ID

git log --stat #show extra information about the commits incluiding how many lines added or removed

git add -p #we will be asked if we accept the changes to be staged

git diff --staged #showing all changes on staged files

git checkout #discard changes in dorking directory before staging it 

git reset HEAD <filename> #revert staging command, like oposite to add

git commit --amend #will Overwrite the previous commit. TRY TO AVOID THIS

git revert HEAD #Create a new commit with the reverse action of the last commit going back to previous files 

git revert 36e86 #Create a new commit with the revert action to a specific previous commit ID identified by 40 character string that we can call by at least 5 charactes 

git branch #list all branches on the repo

gir branch new_feature #Create anew branch 

git checkout new_feature #switch over to the mentioned branch

git checkout -b even_better_feature #Create a and switch over mentioned new branch

git branch -d new_feature #Delete mentioned branch

git merging even_better_feature #Combine branch data to the current branch

'
MERGE CONFLICT:
git status #show detailed information 
git will add some lines to mark the lines in conflict and we can decide what to do with it 
'

git log --graph --oneline #this command will show a graphicall description of the git history on current branch

git merge --abort #this will stop the merge and reset the files on your working tree back the previous commit on your working branch

######## Remote Repos

git clone https://acardogo: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@github.com/jcardogo/DevOps.git #This command contains the PAT (Personal Access Token) and the url to access the remote repo on github

git push #this command will send a commit to be published on remote repo 

git pull #(fetch+Merge) This command will bring  remote repo commit to our local working tree

git remote -v #print the url where wea re pulling code from and also the url where we are pushing to

git remote show origin #Show details about the fetch remote repository and MAIN branches

git branch -r #

git fetch #to check remote repo changes before merging to out local 

git checkout #see the working tree on our local from remote

git log origin/master #to see the commit history of a specific branch 

git status #will tell us if we have any commit (remote) that is not updated on our local branch

git merge origin/master #to merge the remote commit in to our local branch now local and remote pointing to the same commit ID

git log -p -1 # showing some details about the changes made on previous commit 

###### REFACTOR USE CASE

git checkout -b refactor # creating a new branch named recator and moving to it on a single command line

'Modify at least one file'

git commit -a -m 'mesage' #commiting to local after any modification on files

"Test changes to be shure it wont affect remote"

git push -u origin refactor # trying to push local repo to a remote

###### REBASE USE CASE: when we want to disconect our branch from his parent and aplly changes to a most recent version of main commit

git checkout master #move to master branch to call the rebase

git pull #bring all files on master branch repo

git log --graph --oneline --all #show a graphic about all branches on local, incluiding recently pulled master, so we decided to rebase our work tree on current master commit

git checkout refactor # to move to refactor branch in order to call rebase of it over master

git rebase master #change the base of refactor branch to a most recent commit from master

git checkout master #returning back tomaster to merge refactor branch into it

git merge refactor #From master branch we merge changes from refactor branch

git push --delete origin refactor #to remove the refactor branch from remote repo

git branch -d refactor #remove local refactor branch

git push # push all refactor changes to remote repo

#### REBASE on single master branch modified by two people simultaneusly

git fetch #to check any changes on current branch from remote repo

git rebase origin/master # to try to merge my changes with the ones made by someone else 

'In case of conflict we can check the file and resolve the conflict manually'

git add <filename> #to stage the conflic resolved file

git rebase --continue #asking to continue with the rebase process on my local repo

git log --graph --oneline #CHeck the graphical description of the branches merged

git push #sending our local branch to remote repo

######## GOOD practices

#1) Pull most recent version of remote repo before starting modifing somethins to avoid possible conflicts  
#2) Avoid accumulate big changes on multiple files each time you try to push code into Remote Repo
#3) When working on a big change is recomended to create a separated new branch 
#4) you should not rebase changes that  have been pushed to remote repos
#5) Having good commit messages is important

######### Colaborating on GitHub
# we can colaborate on someone else repo by forking (Generating a copy of the repo for my user that could be merged when original owner accepts it) on web browser app
git checkout -p add-readme #wew create a branch to add our new file README file 

git commit -m 'Add a simple README.md file'

git push -u origin add-readme #push to my remote repo, now it is available on web github app

#now from web github app we can create a pull request to the owner of original repo incluiding detail, it is important to check that the commit has no conflict, otherwise we should rebase our commit to the most recent version of owner repo
git rebase -i #to rebase over other type of options that will be shown to select

git status #to check what git show us about our repository 

git log --graph --oneline --all -4 #to see the graphicall image of our repo branches

git push -f #to force our push as is 

### Code Review

#code stryle gide PIP8 https://github.com/google/styleguide

git commit -a --amend #to modify commit message incluidin all comment from modification after revision

git status #to check our repo

git push -f #to send our changes to the remote repository with forced to aplly recent changes

######### MANAGING PROJECTS

# Documentation is key  -------> Communication platforms and methods
# Issue tracker -------> task, goal, resposible (bugzilla) 
# Coordination 

















