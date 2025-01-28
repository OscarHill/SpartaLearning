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

### What is version control?
- It's good for anyone who creates content
	- Remembers each version update and provides a history of all changes - allowing you to go back to earlier versions
- Can provide an off-site copy of data that syncs with a local copy
- It also facilitates collaboration
	- People can update simultaneously and make overlapping changes - Git can help resolve merging and version conflict

### What is Git?
- It's the most popular version control system
- Open source and free
- Comes with a command-line user interface called Git bash
	- all commands can be run via this
- You can use a Git server to copy data
	- Many people use an internet solution - GitHub, GitLab, BitBucket
- Graphical UIs can also be used
	- GitHub desktop, IDE integration
- A directory or folder controlled by Git is called a 'repository' (or just 'repo')


### Creating a Git repository
- the name for the file that excludes files from version control is .gitignore
- Don't put passwords in the repository - which is a use case for ignoring them


### Staging and Committing Files
- The working directory is just where you're doing your programming or whatever
- The staging area or index is where you choose what files you put into the repository
- you would have a repository README file 


### Copying a local repo to GitHub
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


### Branches
- Branches:
	- making branches from the original branch so you can mess around and experiment 
	- if it all goes wrong - you can just stop using that branch and go back to the original version

### The Git Workflow
Here you can see a diagram of the typical git workflow and commands:
![](Git Diagram.png)
- Starting with the files on your local machine in the working directory, you can use `git add` to put those files into the **staging area**
- Now that those files are tracked, implement them to your local repository by using `git commit`
- If you then would like to put those files on an online or remote repo, use `git push` to send those changes over
- Update your local version of an online repository using `git pull` 
- `git checkout` is used to switch to another branch and put it in your working directory
- `git merge <branchname>` is for combining two branches together

### The Collaborative Git Workflow
- The first component is a **Git Authority** - a person who is in charge of the repo and creates it on their GitHub account
  - Their responsibilities including making dev branches, ensuring branch protection is in place, reviewing merges, and setting the default branch
- Team members can then clone the project locally including creating their own feature/dev branches and developing their code their
  - They should **NOT** code directly onto `main` or `dev` as adding code to them without reviewing could damage the project
- On a day-to-day basis:
  - Get the latest dev branch changes by switching to `dev` on your machine and pulling from GitHub
  - Resolve any conflicts
  - Then merge `dev` with `your-feature-branch` to ensure there are no conflicts and everything runs okay
  - Finally when you're done coding - push `your-feature-branch` to GitHub
  - If you want to ship your features to `dev`, then open a pull request on GitHub and get it all reviewed
  - Then repeat - update your local dev branch by `git pull`ing from GitHub

