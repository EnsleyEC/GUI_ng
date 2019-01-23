from db import Database

def main():
    
    ng = Database("http://localhost:11002/","neo4j","ensleyn")
    ng._create_two_nodes("Game","Mario","Player","Ensley","JOGA")

if __name__ == "__main__":
    main()
