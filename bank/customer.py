import pandas as pd
import json

class Customer:

    def __init__(self, customer, accounts):
        self.customer = customer # series
        self.accounts = accounts # dataframe

    def add_amount(self, a_id, amount):
        if a_id in self.accounts.index:
            self.accounts.loc[a_id,'amount'] += amount
            self.customer['total_amount'] = self.get_total_amount()
            self.customer['rat'] = self.get_rat()
        else:
            print("해당 계좌가 없습니다.")

    def sub_amount(self, a_id, amount):
        if a_id in self.accounts.index:
            self.accounts.loc[a_id,'amount'] -= amount
            self.customer[a_id,'total_amount'] = self.get_total_amount()
            self.customer[a_id,'rat'] = self.get_rat()
        else:
            print("해당 계좌가 없습니다.")
    def add_account(self, a_id,a_df):
        if a_id in self.accounts.index :
            print("해당 계좌가 이미 있습니다.")
            pass
        else:
            pass


    def get_total_amount(self):
        return self.customer['total_amount']

    def get_rat(self):

        total_amount = self.get_total_amount()
        if total_amount > 100000:
            rat = 'vvip'
        elif total_amount > 10000:
            rat = 'vip'
        elif total_amount > 1000:
            rat = 'gold'
        elif total_amount > 100:
            rat = 'silver'
        else:
            rat = 'bronze'

        return rat

    def update(self, c_df, a_df):
        c_df.loc[self.customer['c_id']] = self.customer
        a_df.update(self.accounts)

    def get_name(self):
        return self.customer['name']

    def get_cid(self):
        return self.customer['c_id']

    def get_accounts(self):
        return self.accounts

    def get_customer(self):
        return self.customer



def create_customer():
    c_name = input('고객 이름 입력:')
    c_id = input('고객 번호 입력:')

    # account_num 과 total_amount ,rat 을 초기화 시켜서 만듦
    customer = {'c_id':c_id,
                'name':c_name,
                'account_num':0,
                'total_amount':0,
                'rat':'normal'}

    c_df.loc[c_id] = customer

    # c_df.loc[c_df['c_id'] == c_id] = customer
    # pd.concat([c_df, pd.DataFrame([customer])], ignore_index=False)
    print('{} 고객이 생성 되었습니다.'.format(c_name))


def create_acount():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        print("없는 고객 번호 입니다.")
        return


    ac_num = input('계좌번호 입력:')
    ac = {'a_id':ac_num,
          'password':ac_num,
          'c_id':customer.get_cid(),
          'amount':0}
    a_df.loc[c_id] = ac
    print('{} 고객의 {} 계좌가 등록되었습니다'
          .format(customer.get_name(),
                  ac_num))


def show_list():
    for customer in c_df.index:
        print('고객이름:{} | 고객번호:{}'
              .format( c_df.loc[customer]['name'],
                       c_df.loc[customer]['c_id']
                      ))


def search_customer(c_id):
    if c_id in c_df.index:
        customer = c_df.loc[c_id]
        accounts = a_df.loc[a_df['c_id'] == c_id]
        return Customer(customer,accounts)
    return None


def show_customer():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    print('{} 고객님 등급:{} 총금액:{} 계좌정보:\n{}'
          .format(customer.get_name(),
                  customer.get_rat(),
                  customer.get_total_amount(),
                  customer.get_accounts()
                  ))


def deposit():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        print("없는 고객 번호 입니다.")
        return
    else :
        acount_num = input('계좌번호 입력:')
        amount = input('입금할 금액 입력:')
        customer.add_amount(acount_num,int(amount))
        customer.update(c_df,a_df)
    pass

def withdraw():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return
    else :
        acount_num = input('계좌번호 입력:')
        amount = input('출금할 금액 입력:')
        customer.sub_amount(acount_num,int(amount))
        customer.update(c_df,a_df)

def ca_merge():
    merge_df = c_df.set_index('c_id').join(a_df.set_index('c_id'))
    merge_df.to_csv('ca_merge.csv',index = False)
    return print(merge_df)


def group_rat_count():
    group = c_df[['c_id','rat']].groupby(by="rat").count()
    group = group.rename(columns = {'c_id':'count'})
    print(group)


if __name__ == '__main__':

    c_df = pd.read_csv('./customers.csv')
    c_df.set_index('c_id',drop=False)
    a_df = pd.read_csv('./accounts.csv')
    a_df.set_index('a_id',drop=False)

    print('1 - 고객 생성')
    print('2 - 계좌 생성')
    print('3 - 입금')
    print('4 - 출금')
    print('5 - 생성된 고객 리스트 출력')
    print('6 - 고객 정보 출력')
    print('7 - csv 파일로 고객 정보 출력')
    print('8 - csv 파일로 계좌 정보 출력')
    print('9 - csv 파일로 고객 - 계좌 정보 출력')
    print('10 - 등급별 고객의 명수 출력')

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요')
        if input1 == '1':
            create_customer()
        elif input1 == '2':
            create_acount()
        elif input1 == '3':
            deposit()
        elif input1 == '4':
            withdraw()
        elif input1 == '5':
            show_list()
        elif input1 == '6':
            show_customer()
        elif input1 == '7':
            c_df.to_csv('customers_v2.csv',index=False)
            print(c_df)
        elif input1 == '8':
            a_df.to_csv('accounts_v2.csv',index=False)
            print(a_df)
        elif input1 == '9':
            ca_merge()
        elif input1 == '10':
            group_rat_count()

        else:
            print('존재하지 않는 명령어 입니다.')