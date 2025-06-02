def barometer_fibonacci(software_version):
    if software_version in [0, 1]:
        return 1
    elif 2 <= software_version <= 32:
        sum = (
            barometer_fibonacci(software_version - 1) +
            barometer_fibonacci(software_version - 2)
        )
        software_version -= 1
        return sum
    
if __name__ == '__main__':
    software_version = int(input())
    print(barometer_fibonacci(software_version))