#9.	Nested Dictionary Access: Work with deeply nested dicts to access or update a value.

nested_dict = {
    'student': {
        'name': 'Deepak',
        'age': 24,
        'address': {
            'city': 'Cuttack',
            'state': 'Odisha',
            'zip': '753001'
        },
        'courses': {
            'data_science': {
                'duration': '6 months',
                'status': 'ongoing'
            },
            'machine_learning': {
                'duration': '6 months',
                'status': 'upcoming'
            }
        }
    }
}
c = nested_dict['student']['address']['city']
print(c)