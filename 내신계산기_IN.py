# -*- coding: euc-kr -*-
#�̹ο�10517_���Ű���

def sh(a,b):
    m = b*a/100
    return m

def zp(a,b):
    m = b*a/100
    return m

def zd(a,b):
    m = 100 * (a-20+b) / a
    return max

print("1: ���� �� ������, 2: ���� �� ������, 3: ���� �������� �� ���� �� ������, 4: ���� �� ���� ��, 5: ��� ���� �ջ� �� ������")
switch = int(input("��带 �Է��ϼ���: "))

if switch == 1: #1: ���� �� ������
    print("<���� �� ������> ��带 �����ϼ̽��ϴ�.")
    print(" ")

    ts_pc = int(input("�߰���� �ݿ� ������ �Է��ϼ���: "))

    print("���� ������ �Է����ּ���(�߰� �⸻) EX) 90 85")

    test_1, test_2 = input().split()
    test_1 = int(test_1)
    test_2 = int(test_2)
    print(" ")

    print("����� ���ʰ�� �������� ",zp(test_1, pt_pc) + zp(test_2, pt_pc),"�Դϴ�.")

elif switch == 2: #2: ���� �� ������
    print("<���� �� ������> ��带 �����ϼ̽��ϴ�.")
    print(" ")
    sh_pc = int(input("������ �ݿ� ������ �Է��ϼ���: "))

    print("���� ������ �Է����ּ���(�������� 100�� �������� ����մϴ�)")
    sh= input()
    sh = int(sh)
    print(" ")

    print("����� ������ ��������", sh(sh, sh_pc), "�Դϴ�.")



elif switch == 3: #3: ���� �������� �� ���� �� ������
    print("<���� �������� �� ���� �� ������> ��带 �����ϼ̽��ϴ�.") 
    print(" ")
    
    sh_pc = int(input("������ �ݿ� ������ �Է��ϼ���: "))

    cnt = 0
    n = int(input("�Է��� ���������� ������ �Է��ϼ���: "))

    print("���������� �Է��ϼ���:")

    k=n
    i=0
    while k>0:
        cnt = cnt + int(input())
        k = k - 1
    avg = cnt / n


    print("����� ������ ��������", sh(avg, sh_pc), "�Դϴ�.")




elif switch == 4: #4: ���� �� ���� ��
    print("<���� �� ���� ��> ��带 �����ϼ̽��ϴ�.") 
    sh_1=[]
    n = int(input("�������� ������ �Է��ϼ���:"))
    print(" ")

    i=0
    cnt = 0
    cnt_ts = 0;
    while n>0:
        print(i+1,"��° ��������(������X)�� �Է��ϼ���:", end='')
        k = int(input())
        print(i+1,"��° ���� ������ �Է��ϼ���:", end='')
        g = int(input())
        cnt_ts = cnt_ts + g
        cnt = cnt + sh(k,g)
        n = n - 1
        i = i + 1
        print(" ")

    j = 100 - cnt_ts
    
    cnt = cnt_ts - cnt

    print(cnt)

    print("����� ���� ���� �� ������ ", zd(j ,cnt), "�Դϴ�.")

elif switch == 5: #5: ��� ���� �ջ� �� ������
    print("<��� ���� �ջ� �� ������> ��带 �����ϼ̽��ϴ�.")   


