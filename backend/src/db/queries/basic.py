from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Balu@2481358"))

def get_friends_of(tx, name):
    friends = []
    result = tx.run("""match p=(a:Person)-[]->(b:Person)

unwind nodes(p) as n unwind relationships(p) as r
with collect( distinct {id: ID( n), name: n.FirstNname}) as nl, 
collect( distinct {source: ID(startnode(r)), target: ID(endnode(r)), strength: r.strength}) as rl
RETURN {nodes: nl, links: rl}""")
    for record in result:
        friends.append(record.data())
    return friends

def get_basic():
    with driver.session() as session:
        result = session.read_transaction(get_friends_of, "Alice")
    return result