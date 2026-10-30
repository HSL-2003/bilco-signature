with open('C:/Users/ITPC/Downloads/hh/server.py', 'r') as f:
    source = f.read()

print('class SignatureHandler in source:', 'class SignatureHandler' in source)

try:
    namespace = {}
    exec(source, namespace)
    print('SignatureHandler in namespace:', 'SignatureHandler' in namespace)
    if 'SignatureHandler' in namespace:
        print('SignatureHandler type:', type(namespace['SignatureHandler']))
except Exception as e:
    print('EXEC ERROR:', repr(e))

# Write output to file
with open('C:/Users/ITPC/Downloads/hh/test_output.txt', 'w') as f:
    f.write('class SignatureHandler in source: ' + str('class SignatureHandler' in source) + '\n')
    try:
        namespace = {}
        exec(source, namespace)
        f.write('SignatureHandler in namespace: ' + str('SignatureHandler' in namespace) + '\n')
    except Exception as e:
        f.write('EXEC ERROR: ' + repr(e) + '\n')

