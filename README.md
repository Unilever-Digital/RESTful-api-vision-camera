Connection API QLT (Quality, Load, and Throughput) is a RESTful API designed to provide insights into the quality, load, and throughput of network connections. It offers a set of endpoints to query and analyze various metrics related to network connections, aiding in monitoring and optimizing network performance.

## Technical stack:
   - Flask
   - gunicorn server
   - MongoDB
   - SQLite

## Installation
1. Clone the repository:

         git clone https://github.com/Unilever-Digital/app-restfulapi-vision-camera.git

2. Install dependencies:

         pip install -r requirements.txt

3. Local runing:

         python main.py
      

5. Access the API endpoints at `http://localhost:8080` by default.

## Source
```
.
├── README.md                 # README file
├── app   
│   └── controls
│   └── models
│   └── static                # Public folder
│     └── images              # Image used by default template for document site (not api site)
│         └── png
│         └── jpg
│         └── svg
│     └── css
│     └── js
│   └── templates             # Template ui for document site (not api site)
│   └── views                 # API
│   └── env.py
├── instance
├── test
├── .gitignore
├── .python-version           # python version define file
├── config.py                 # config backend server file
├── Dockerfile                # Dockerfile
├── docker-compose.yml        # docker-compose configuration
├── main.py                   # running file
├── package.json              # config file
├── Procfile                  # config file for running in Gunicorn server
├── requirements.txt          # list python lib file
└── ...                       # Other configuration files (prettier, ignore files,...)
```

## Authentication
Authentication is required to access the API endpoints. Include the authentication token in the request headers to authenticate.

## Contributors
- [Le Chon Minh Dat](https://github.com/lcmd65)
- [Nguyen Minh Hieu](https://github.com/BanhBaoa)
- [...]

## License
This project is licensed under the [MIT License](LICENSE).

## Support
For support or inquiries, please contact [Le-chon-minh.dat@unilever.com](mailto:Le-chon-minh.dat@unilever.com).
