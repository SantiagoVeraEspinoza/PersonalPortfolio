from datetime import datetime

def get_requests_in_time_range(log_file, start_time, end_time):
    requests = []
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    with open(log_file) as f:
        for line in f:
            fields = line.split()
            timestamp = fields[3][1:]
            request_time = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S')
            if start_time <= request_time <= end_time:
                requests.append(line)

    return requests

log_file = './apache_access'
start_time = '2021-05-30 12:22:00'
end_time = '2021-05-30 12:33:12'

requests_in_range = get_requests_in_time_range(log_file, start_time, end_time)
for request in requests_in_range:
    print(request)
