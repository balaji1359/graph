from neo4j import GraphDatabase

uri = "neo4j://3.19.26.1:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Balu@2481358"))

def get_friends_of(tx, name):
    friends = []
    result = tx.run("""match p=(a:Person)-[]->(b:Book)
unwind nodes(p) as n unwind relationships(p) as r
with collect( distinct {id: ID( n), 
label:labels(n), name: n.FirstNname, 
gender:n.Gender, title:n.title}) as nl, 
collect( distinct {source: ID(startnode(r)), target: ID(endnode(r))}) as rl
RETURN {nodes: nl, links: rl}""")
    for record in result:
        friends.append(record.data())
    return friends

def get_basic():
    with driver.session() as session:
        result = session.read_transaction(get_friends_of, "Alice")
    return result[0]['{nodes: nl, links: rl}']
