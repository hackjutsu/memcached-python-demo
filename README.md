# Demo for pylibmc

Launch the memcached server
```bash
memcached -d
```

Set up python virtual environment
```bash
virtualenv ENV
. ENV/bin/activate
```

Install dependencies
```bash
brew install libmemcached
pip install -r requirements.txt
```

Run the code
```bash
python py-memcached.py
```

## License
MIT
