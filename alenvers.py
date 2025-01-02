import socket, time, re

def listen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    while True:
        data = s.recv(1024).decode().strip()
        print(f"data: {data}")
        if re.search(r"FCSC\{.*\}", data) is not None:
            break
        word = re.search(r">>> (.*)$", data).group(1)
        print(f"word: {word}")
        answer = word[::-1] + "\n"
        print(f"answer: {answer.encode("utf-8")}")
        s.sendall(answer.encode("utf-8"))
        time.sleep(0.1)
    s.close()

listen("127.0.0.1",4000)

