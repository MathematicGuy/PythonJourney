def main():
    print('Hi Candace')


'''
    
 If __main__ is running, activate main()
 What ( if __name__ == '__main__': )  telling us is:
 + Is Josh.py running or is it imported
 Có thể dùng để chỉ chạy code trong file hiện tại. Ko chạy code Import
 '''

if __name__ == '__main__':
    main()
elif __name__ != '__main__':
    print('Currently running module: {}'.format(__name__))

