### Notes on Sparta Global Git Fundamentals Course
##### Course Agenda
- What is version control?
- What is Git?
- Installing Git on Windows
- Creating a Git repository
- Staging & committing files in Git
- Creating a GitHub account
- Copying a local repo to GitHub
- Coping a GitHub repo locally
- Synchronising local and remote repo copies
- What next?

##### What is version control?
- It's good for anyone who creates content
	- Remembers each version update and provides a history of all changes - allowing you to go back to earlier versions
- Can provide an off-site copy of data that syncs with a local copy
- It also facilitates collaboration
	- People can update simultaneously and make overlapping changes - Git can help resolve merging and version conflict

##### What is Git?
- It's the most popular version control system
- Open source and free
- Comes with a command-line user interface called Git bash
	- all commands can be run via this
- You can use a Git server to copy data
	- Many people use an internet solution - GitHub, GitLab, BitBucket
- Graphical UIs can also be used
	- GitHub desktop, IDE integration
- A directory or folder controlled by Git is called a 'repository' (or just 'repo')

##### Installing Git
- Branches:
	- making branches from the original branch so you can mess around and experiment 
	- if it all goes wrong - you can just stop using that branch and go back to the original version
- 


##### Creating a Git repository
- the name for the file that excludes files from version control is .gitignore
- Don't put passwords in the repository - which is a use case for ignoring them


##### Staging and Committing Files
- The working directory is just where you're doing your programming or whatever
- The staging area or index is where you choose what files you put into the repository
- you would have a repository README file 


##### Copying a local repo to GitHub
- git add sends it to staging, git commit sends it to a local repo, git push sends it to GitHub
- make sure that any files with secrets in aren't in the ls-files
- Order of operations:
	- Copy the https URL
	- In git bash set the connection to GitHub
		- `git remote add origin <url>
	- Push the changes to GitHub
		- `git push origin main
	- When prompted, choose the token option
		- create the token on github
	- All tracked files will be copied to github
- Or:
	- Copy the SSH URL from the quick setup page
	- in git bash set the connection to GitHub
		- `git remote add origin <url>`
	- Create the keys using ssh-keygen
		- remember the passphrase!
	- Copy the public key
	- add it to github
	- push the changes to github
		- `git push origin main

(important to be able to do git init, git add, git commit, git push)
