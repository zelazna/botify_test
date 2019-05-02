# Install

run the install script:  
```bash 
scripts/install.sh
```

Then wait for the end of the import, `Towns imported successfully` should be printed 

# Launch

run the run script:  
```bash 
scripts/run.sh
```

# Run with docker

## build image

```bash
docker build -t botify_test . 
```

## run it

```bash
docker run botify_test -p 8080:8080
```

