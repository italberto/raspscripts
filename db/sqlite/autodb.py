# -*- coding: utf-8 -*-

#      __             ___    __                     __
#   __/\ \__         /\_ \  /\ \                   /\ \__
#  /\_\ \ ,_\    __  \//\ \ \ \ \____     __   _ __\ \ ,_\   ___
#  \/\ \ \ \/  /'__`\  \ \ \ \ \ '__`\  /'__`\/\`'__\ \ \/  / __`\
#   \ \ \ \ \_/\ \L\.\_ \_\ \_\ \ \L\ \/\  __/\ \ \/ \ \ \_/\ \L\ \
#    \ \_\ \__\ \__/.\_\/\____\\ \_,__/\ \____\\ \_\  \ \__\ \____/
#     \/_/\/__/\/__/\/_/\/____/ \/___/  \/____/ \/_/   \/__/\/___/
#
#


# Author: Italberto Figueira Dantas
# Requirements: python3.x

import sqlite3
import re      #regex support
from time import gmtime, strftime

# Recebe como parâmetros na inicialização o nome da tabela e os campos que irão compor a tabela
# e através do método __str__ retorna a string com o comando sql para criar a tabela.
class TableDefinition:



    def __init__(self,name,fields={}):
        self.name = name
        self.fields = fields

    def __str__(self):
        ret = 'CREATE TABLE IF NOT EXISTS '+self.name+' (*content*);'
        content = ''
        for f in self.fields.keys():
            content += str(f) + ' ' + str(self.fields[f])+','

        content = re.sub(',$', '', content)
        #content = content.replace('$,','')
        ret = ret.replace('*content*',content)

        return ret


# Classe que representa um banco e as operações que podem realizadas sobre ele.
class DB:


    # Nome do banco padrão é database.db
    def __init__(self,database_name='database.db',table_list=[]):
        self.print_commands = False
        self.conn = sqlite3.connect(database_name)
        self.table_list = table_list
        self.initializedb()


    def initializedb(self):
        c = self.conn.cursor()
        if not self.checkdb():
            try:
                #percorre as definições de tabelas e cria todas as tabelas definidas na inicialização da classe.
                for t in self.table_list:
                    self.show(str(t))
                    c.execute(str(t))

            except sqlite3.OperationalError as e:
                print(e)

    def checkdb(self):
        True

    # Encerra a conexão com o banco
    def close(self):
        if self.conn:
            self.conn.close()

    # executa o comando de select
    def select(self,table='',conditions={}):
        com = 'SELECT * FROM ' + table

        if len(conditions)>0:
            com += ' WHERE *conditions*'

            condi = ''

            for x in conditions.keys():
                join = ' = '

                if str(conditions[x]).lower() in ['true', 'false']:
                    join = ' is '

                condi += str(x) + join + conditions[x] + ' and'

                condi = re.sub('and$', '', condi)

                com = com.replace('*conditions*', condi)

        return self.exec_select(com)



    # Executa um comando de update no banco
    def update(self,table,field_values={},conditions_values={}):
        cm = 'UPDATE ' + table + ' SET *fields* WHERE *conditions*;'

        fields = ''
        conditions = ''

        for x in field_values:
            fields += str(x) + ' = ' + field_values[x] + ','

        fields = re.sub(',$','',fields)
        #fields = fields.replace('$,','')

        for x in conditions_values:
            conditions += str(x) + ' = ' + conditions_values[x] + ','

        conditions = re.sub(',$','',conditions)
        #conditions = conditions.replace('$,', '')

        self.exec_command(cm.replace('*fields*',fields).replace('*conditions*',conditions))


    #Executa um comando de insert em uma tabela
    def insert(self,table='',field_value={}):
        com = 'INSERT INTO '+ table + '(*fields*) VALUES (*values*);'

        fields = ''
        values = ''

        for x in field_value.keys():
            fields += str(x) + ','
            values += str(field_value[x]) + ','


        fields = re.sub(',$','',fields)
        values = re.sub(',$','',values)

        self.exec_command(com.replace('*fields*',fields).replace('*values*',values))



    def delete(self,table,conditions):
        com = 'DELETE FROM '+table+ ' WHERE *conditions*'
        condi = ''

        for x in conditions.keys():
            join = ' = '

            if str(conditions[x]).lower() in ['true','false']:
                join = ' is '

            condi += str(x) + join + conditions[x] + ' and'

        condi = re.sub('and$','',condi)

        self.exec_command(com.replace('*conditions*',condi))



    def exec_select(self,command):
        self.show("SQL command: ["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]: " + command)
        c = self.conn.cursor()
        try:
            c.execute(command)
        except sqlite3.OperationalError as e:
            print(e)

        return c.fetchall()


    def exec_command(self,command):
        self.show("SQL command: ["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]: " + command)

        c = self.conn.cursor()
        try:
            c.execute(command)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)


    def show(self,command):
        if self.print_commands:
            print(command)

class iDb(DB):

    def __init__(self,dbname,table_list):
        table_list.append(TableDefinition('tcheck', {'id': 'integer'}))
        super().__init__(dbname,table_list)


    def checkdb(self):
        c = self.conn.cursor()
        try:
            c.execute('''SELECT id FROM tcheck;''')
            return True
        except sqlite3.OperationalError as e:
            return False
        # return False






# main
table_list = [TableDefinition('history', {'id': 'integer', 'texto': 'text'})]

x = iDb('shell.db',table_list)

x.print_commands = True



x.close()