#!python3
#encoding:utf-8
import subprocess
import shlex
import os.path
import getpass
import language.insert.Main
import gnu_license.create.Main
import gnu_license.insert.main
import license.insert.Main
class InitializeMasterDbCreator:
    def __init__(self, db_dir_path):
        self.db_dir_path = db_dir_path
        self.db_files = [
#            'GitHub.Languages.sqlite3': CreateLanguage,
#            'GitHub.Licenses.sqlite3': self.CreateLicenses,
            {'FileName': 'GitHub.Languages.sqlite3', 'Creator': self.__CreateLanguages, 'Inserter': self.__InsertLanguages},
            {'FileName': 'GNU.Licenses.sqlite3', 'Creator': self.__CreateGnuLicenses, 'Inserter': self.__InsertGnuLicenses},
            {'FileName': 'GitHub.Licenses.sqlite3', 'Creator': self.__CreateLicenses, 'Inserter': self.__InsertLicenses},
#            'GitHub.Accounts.sqlite3': CreateAccounts,
#            'GitHub.Repositories.{user}.sqlite3': CreateRepositories,
#            'GitHub.Repositories.__other__.sqlite3': CreateOtherRepositories,
#            'GNU.Licenses.sqlite3': CreateGnuLicenses,
#            'GitHub.Api.sqlite3': CreateApi
        ]

    def Run(self):
        if not(os.path.isdir(self.db_dir_path)):
            print('DBディレクトリを作る----------------')
            os.mkdir(self.db_dir_path)
        for db in self.db_files:
            db_path = os.path.join(self.db_dir_path, db['FileName'])
            if not(os.path.isfile(db_path)):
                print('DBファイルを作る: {0} ----------------'.format(db_path))
                db['Creator'](db_path)
                db['Inserter'](db_path)

    def __CreateLanguages(self, db_path):
#        creator_language = language.create.Main.Main(db_path)
#        creator_language.Run()
        subprocess.call(shlex.split("bash ./language/create/Create.sh \"{0}\"".format(db_path)))

    def __InsertLanguages(self, db_path):
        creator_language = language.insert.Main.Main(db_path)
        creator_language.Run()

    def __CreateGnuLicenses(self, db_path):
#        subprocess.call(shlex.split("bash ./gnu_license/create/Create.sh \"{0}\"".format(db_path)))
        creator_language = gnu_license.create.Main.Main(db_path)
        creator_language.Run()

    def __InsertGnuLicenses(self, db_path):
        creator_gnu_license = gnu_license.insert.main.GnuSite(db_path)
        creator_gnu_license.GetAll()

    def __CreateLicenses(self, db_path):
        subprocess.call(shlex.split("bash ./license/create/Create.sh \"{0}\"".format(db_path)))

    def __InsertLicenses(self, db_path):
        creator_license = self.__LicenseCreator(db_path)
        creator_license.Initialize()

    def __LicenseCreator(self, db_path):
        github_user_name = 'ytyaru'
        os_user_name = getpass.getuser()
        device_name = '85f78c06-a96e-4020-ac36-9419b7e456db'
        path_db_base = 'mint/root/db/Account/GitHub'
        path_db_account = '/media/{0}/{1}/{2}/private/v0/GitHub.Accounts.sqlite3'.format(os_user_name, device_name, path_db_base)
        path_db_repo = '/media/{0}/{1}/{2}/public/v0/GitHub.Repositories.{3}.sqlite3'.format(os_user_name, device_name, path_db_base, github_user_name)
        return license.insert.Main.Main(github_user_name, path_db_account, path_db_repo, db_path)
