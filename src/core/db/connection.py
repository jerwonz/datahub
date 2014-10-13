import psycopg2
import re

from backend.pg import PGBackend

'''
@author: anant bhardwaj
@date: Oct 3, 2013

DataHub DB wrapper for backends (only postgres implemented)
Any new backend must implement the DataHubConnection interface
'''

class DataHubConnection:
  def __init__(self, user, password, repo_base=None):
    self.backend = PGBackend(user, password, repo_base=repo_base)
  
  def reset_connection(self, repo_base):
    self.backend.reset_connection(repo_base=repo_base)

  def close_connection(self):    
    self.backend.close_connection()

  def create_repo(self, repo):
    return self.backend.create_repo(repo=repo)

  def list_repos(self):
    return self.backend.list_repos()

  def delete_repo(self, repo, force=False):
    return self.backend.delete_repo(repo=repo, force=force)

  def share_repo(self, repo, username, auto_in_future=True):
    return self.backend.share_repo(
        repo=repo, username=username, auto_in_future=auto_in_future)

  def list_tables(self, repo):
    return self.backend.list_tables(repo=repo)

  def print_schema(self, table):
    return self.backend.print_schema(table=table)

  def execute_sql(self, query, params=None):
    return self.backend.execute_sql(query, params)

  def has_connect_privilege(self, login, privilege):
    return self.backend.has_connect_privilege(
        login=login, privilege=privilege)

  def has_repo_privilege(self, login, repo, privilege):
    return self.backend.has_repo_privilege(
        login=login, repo=repo, privilege=privilege)

  def has_table_privilege(self, login, table, privilege):
    return self.backend.has_table_privilege(
        login=login, table=table, privilege=privilege)

  def has_column_privilege(self, login, table, column, privilege):
    return self.backend.has_column_privilege(
        login=login, table=table, column=column, privilege=privilege)


  '''
  The following methods works only in superuser mode
  '''

  def create_user(self, username, password):
    return self.backend.create_user(username, password)

  def change_password(self, username, password):
    return self.backend.change_password(username, password)

  def import_file(self, table_name, file_path):
    return self.backend.import_file(table_name=table_name, file_path=file_path)

  def export_file(self, table_name, file_path):
    return self.backend.export_file(table_name=table_name, file_path=file_path)

  def list_shared_repos(self, username):
    return self.backend.list_shared_repos(username)