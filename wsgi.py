from jiublog import create_app

app = create_app('production')
if __name__ == '__main__':
    app.run(host='10.3.3.49', port=5005)