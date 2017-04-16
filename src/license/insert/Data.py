#!python3
#encoding:utf-8
import os.path
import subprocess
import dataset

class Data:
    def __init__(self, user_name, path_db_account, path_db_repo, path_db_license):
        self.user_name = user_name
        self.db_license = dataset.connect('sqlite:///' + path_db_license)
        self.db_acc = dataset.connect('sqlite:///' + path_db_account)
        self.db_repo = dataset.connect('sqlite:///' + path_db_repo)
    def get_username(self):
        return self.user_name
    def get_ssh_host(self):
        return "github.com.{0}".format(self.user_name)
    def get_mail_address(self):
        return self.db_acc['Accounts'].find_one(Username=self.get_username())['MailAddress']
    def get_access_token(self, scopes=None):
        sql = "SELECT * FROM AccessTokens WHERE AccountId == {0}".format(self.db_acc['Accounts'].find_one(Username=self.get_username())['Id'])
        if not(None is scopes):
            sql = sql + " AND ("
            for s in scopes:
                sql = sql + "(',' || Scopes || ',') LIKE '%,{0},%'".format(s) + " OR "
            sql = sql.rstrip(" OR ")
            sql = sql + ')'
        return self.db_acc.query(sql).next()['AccessToken']
    def get_repo_name(self):
        return os.path.basename(self.path_dir_pj)        
    def get_repo_description(self):
        return self.description
    def get_repo_homepage(self):
        return self.homepage

