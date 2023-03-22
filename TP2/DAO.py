
import sqlite3

import os.path


FK_ON = 'PRAGMA foreign_keys = ON;'

CREER_UNIQUE_WORDS= '''

CREATE TABLE IF NOT EXISTS tb_unique_words
(
    id integer PRIMARY KEY AUTOINCREMENT,
    nom char(255) UNIQUE NOT NULL 
    
)'''

CREER_STOP_WORDS = '''

CREATE TABLE IF NOT EXISTS tb_stop_words

    (
    id INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
    mots CHAR(255) UNIQUE NOT NULL
    )

'''

CREER_COOCURRENCES = '''

CREATE TABLE IF NOT EXISTS tb_coocurrences

    (
    id_mot INTEGER NOT NULL ,
    id_mot2 INTEGER NOT NULL ,
    taille_fenetre INTEGER NOT NULL,
    frequence INTEGER NOT NULL,
    
    PRIMARY KEY (id_mot,id_mot2, taille_fenetre),
    CONSTRAINT FK_mot1 FOREIGN KEY (id_mot) REFERENCES tb_unique_words(id),
    CONSTRAINT FK_mot2 FOREIGN KEY (id_mot2) REFERENCES tb_unique_words(id)
    )

'''

INSERT_MOTS_UNIQUE = "INSERT OR REPLACE INTO tb_unique_words VALUES(?,?)"
INSERT_STOP_WORDS = "INSERT OR REPLACE INTO tb_stop_words(id,mots) VALUES(?,?)"
INSERT_COOCURRENCES = "INSERT OR REPLACE INTO tb_coocurrences(id_mot, id_mot2, taille_fenetre, frequence) VALUES(?,?,?,?)"



DELETE_COOCURRENCES = 'DELETE from tb_coocurrences'
DELETE_DATA_COOCURRENCES = 'DELETE from tb_coocurrences'
DELETE_DATA_UNIQUEWORD = 'DELETE from tb_unique_words'

SELECT_UNIQUE_WORDS ='SELECT id, nom FROM tb_unique_words'
SELECT_STOP_WORDS ='SELECT * FROM tb_stop_words'
SELECT_WORDS_FROM_STOP_WORD = 'SELECT mots FROM tb_stop_words'

SELECT_COOCURENCE = 'SELECT id_mot, id_mot2, frequence, taille_fenetre FROM tb_coocurrences'
SELECT_ID_UNIQUE_WORDS ='SELECT id FROM tb_unique_words'

#revoie tous les mots selon une taille de fenetre
SELECT_NOM_SELON_FENETRE = 'SELECT DISTINCT nom FROM tb_unique_words INNER JOIN tb_coocurrences ON tb_unique_words.id = tb_coocurrences.id_mot WHERE tb_coocurrences.taille_fenetre = ?'

FUSION = 'DELETE FROM tb_unique_words WHERE (nom) IN (SELECT mots FROM tb_stop_words);'
UPDATE = 'UPDATE tb_unique_words SET noms = ? (noms)'
class Dao():

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_dir = (BASE_DIR + '\\coo.db')
        self.chemin_bd = db_dir
        self.bool = True
        self.connexion()
        self.creer_bd()

    def connexion(self):
        self.conn = sqlite3.connect(self.chemin_bd)
        self.cur = self.conn.cursor()
        self.cur.execute(FK_ON)
        # self.cur.execute(FK)

    def deconnexion(self):
        self.cur.close()
        self.conn.close()

    def creer_bd(self):
        self.cur.execute(CREER_UNIQUE_WORDS)
        self.cur.execute(CREER_STOP_WORDS)
        self.cur.execute(CREER_COOCURRENCES)

    def insert_words_unique(self, data):
        self.cur.executemany(INSERT_MOTS_UNIQUE, data)
        self.conn.commit()

    def insert_stop_words(self, id, stop_words):
        self.cur.execute(INSERT_STOP_WORDS, (id, stop_words))
        self.conn.commit()

    def fetch_all_unique_words(self):
        tab = []
        self.cur.execute(SELECT_UNIQUE_WORDS)
        tab = self.cur.fetchall()
        return tab

    def fetch_all_stop_words(self):
        self.cur.execute(SELECT_STOP_WORDS)
        return self.cur.fetchall()

    def fetch_nom_stop_word(self):
        self.cur.execute(SELECT_WORDS_FROM_STOP_WORD)
        return self.cur.fetchall()

    def fetch_coocurrence(self):
        self.cur.execute(SELECT_COOCURENCE)
        return self.cur.fetchall()

    def fetch_id_unique_words(self):
        self.cur.execute(SELECT_ID_UNIQUE_WORDS)
        return self.cur.fetchall()

    def fetch_mots_selon_taille_fenetre(self, taille_fenetre):
        self.cur.execute(SELECT_NOM_SELON_FENETRE, (taille_fenetre,))
        return self.cur.fetchall()

    def inserer_datas(self, data):
        self.insert_words_unique(data)

    #id_mot, id_mot2, taille, frequence

    def insert_coocurrences(self, data):
        self.cur.executemany(INSERT_COOCURRENCES, data)
        self.conn.commit()

    def fusion_tables(self):
        self.cur.execute(FUSION)
        self.conn.commit()

    def delete_table_coocurrence(self):
        self.cur.execute(DELETE_COOCURRENCES)
        self.conn.commit()

    def delete_and_recreate(self):
        self.cur.execute(DELETE_DATA_COOCURRENCES)
        self.cur.execute(DELETE_DATA_UNIQUEWORD)
        self.conn.commit()