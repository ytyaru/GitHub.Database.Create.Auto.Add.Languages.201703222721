#!python3
#encoding:utf-8
import sys
import subprocess
import shlex
import os.path
import getpass
import dataset
class tsv2sqlite3:
    def __init__(self):
        self.delimiter = '\t'

    def Run(self):
        self.__CheckParameters()
        self.db.begin()
        self.__Insert()
        self.db.commit()
        
    def __CheckParameters(self):
        print(len(sys.argv))
        for a in sys.argv:
            print(a)
        if len(sys.argv) < 4:
            raise Exception("'python3 tsv2insert.py {TSVファイルパス} {SQLite3ファイルパス} {テーブル名}'のように引数を指定してください。")
        
        self.path_tsv = sys.argv[1]
        self.path_db = sys.argv[2]
        self.name_table = sys.argv[3]
        
        if not(os.path.isfile(self.path_tsv)):
            raise Exception("第一引数のファイルは存在しません。存在するTSVファイルを指定してください。: {0}".format(self.path_tsv))
        if not(os.path.isfile(self.path_db)):
            raise Exception("第二引数のファイルは存在しません。存在するSQLite3のDBファイルを指定してください。: {0}".format(self.path_db))
        
        self.db = dataset.connect('sqlite:///' + self.path_db)
        self.table = self.db[self.name_table]
        
    def __Insert(self):
        with open(self.path_tsv, mode='r', encoding='utf-8') as f:
            line = f.readline().rstrip('\r\n') # 末尾の`\r`と`\n`をすべて削除する
            columns = line.split(self.delimiter)
            while line:
                line = f.readline().rstrip('\r\n') # 末尾の`\r`と`\n`をすべて削除する
                print(line)
                record = self.__CreateRecord(columns, line)
                if None is not record:
                    self.table.insert(record)
    
    def __CreateRecord(self, columns, line):
        datas = line.split(self.delimiter) # 最後の改行をとる
        if len(columns) != len(datas):
            print('以下の行は列ヘッダと数が合わないため処理しません。')
            print(line)
            return None
        col_count = 0
        record = {}
        for col_count in range(0, len(columns)):
            record[columns[col_count]] = datas[col_count]
        print(record)
        return record

if __name__ == "__main__":
    main = tsv2sqlite3()
    main.Run()
