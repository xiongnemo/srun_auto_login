# srun_auto_login
Auto login script for Srun's (深澜软件) campus network authentication system.

## Prerequisites

`python3`

## Config File Format

```json
{
    "TARGET_ENDPOINT": "******",       // your srun endpoint
    "USE_HTTPS": false,                // whether you use https
    "USERNAME": "******",              // your srun username
    "PASSWORD": "****"                 // your srun password
}
```

## Run

### Just Run

```bash
python3 ./main.py
```

### Cron

* Default cron configuration is `At minute 0 past every 4th hour`.
* Make sure current directory is R/W, or you may want to update the script.

```bash
chmod +x cron.sh # if you took the file from Windows 
./cron.sh
```

### Loop

* Find a useable terminal or make it background.

```bash
./loop.sh
# or
./watch.sh
```