![banner](https://github.com/mk3-14159/Winniepotv2/blob/master/banner/README_Banner.png)

# Download Instructions  
---

## Step 1 - git-download

1. Update system software by running

```sh
sudo apt-get update
```

2. Downloads a remote git repository into a directory or into a `tar` file. Provides a wrapper around the `git archive` command, executing a command like this from node:

```sh
sudo apt install git-all
```

**NOTE:** Github does not support `git archive`, so this package does not work with Github repos. This package can be used to download git repositories from private git servers as well as Atlassian Stash and Bitbucket. It may be enhanced to add github support in the future using a different download method.

3. Check git version 

```sh
git --version 
```

## Step 2 - Winniepot Installation

Download Winniepot from the Winniepotv2 repository

```sh
git clone https://github.com/mk3-14159/Winniepotv2.git
```

## Step 3 - Usage 

1. Once Winniepot is installed cd into the Winniepot repository

```sh
cd Winniepotv2
```

2. Deploy Winniepot to the endpoint (ip address) that you are hosting with the corresponding port eg. port 9000

```sh
python3 winniepot.py 9000
```



## Credits

```
 _     _  ___   __    _  __    _  ___   _______  _______  _______  _______
| | _ | ||   | |  |  | ||  |  | ||   | |       ||       ||       ||       |
| || || ||   | |   |_| ||   |_| ||   | |    ___||    _  ||   _   ||_     _|
|       ||   | |       ||       ||   | |   |___ |   |_| ||  | |  |  |   |  
|       ||   | |  _    ||  _    ||   | |    ___||    ___||  |_|  |  |   |  
|   _   ||   | | | |   || | |   ||   | |   |___ |   |    |       |  |   |  
|__| |__||___| |_|  |__||_|  |__||___| |_______||___|    |_______|  |___|  

NUIG FYP Honeypot Group (Coordinator: Martin Hughes) 
(c) MK Chong 2022
```
[original repo](https://github.com/mk3-14159/Winnie)

 
