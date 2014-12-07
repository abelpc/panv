#!/usr/bin/python

import sys
import subprocess
import copy

IP_SCRIPT="../get_ip.sh"
SEPARATOR="/"
LIST_CMD = "ls"
RESULTS_DIR = sys.argv[1]

p = subprocess.Popen([LIST_CMD, RESULTS_DIR], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
dirs, err = p.communicate()
nodes = dirs.splitlines()

columns = {}
rows = {}

for node in nodes:
	name = node.replace(".pcap.stats", '')
	columns[name] = 0
	rows[name] = 0

for node in nodes:
	name = node.replace(".pcap.stats", '')
	columns[name] = copy.deepcopy(rows)


for node in nodes:

	file = RESULTS_DIR + SEPARATOR + node
	node_file = open(file, 'r')
	node_connections = node_file.read().splitlines()
	node = node.replace(".pcap.stats", '')

	for connection in node_connections:

		#print "Columns_keys: \n %i\n\n" % len(columns.keys())
		if not (columns.has_key(connection)):
			rows[connection] = 0
			columns[connection] = copy.deepcopy(rows)
			#print "Nova coluna (%s): %s\n\n" % (connection, columns[connection])
			#print "New_Columns_keys: %i \n" % len(columns.keys())

			for all in columns.keys():

				#print "Adding %s (%s)" % (all, node)

				#if (all == node):
				#	columns[node][connection] = 1
				#else:
					#temp3 = copy.deepcopy(columns[all])
					#temp3[connection] = 0
				columns[all][connection] = 0
		#else:
		columns[node][connection] = 1

	#print "%s\n" % node 
	#print rows
	#print columns[node]

first_row = " "
for x in columns.keys():
	first_row = first_row + "%s " % x

print first_row

for x in columns.keys():
	coluna = x + "\t"

	#print "%s \n\n %s\n\n" % (x, columns[x])
	for y in columns[x].keys():
		#if (x == y):
		#	coluna = coluna + str(columns[x][y]) + "(x) "
		#else:
		coluna = coluna + str(columns[x][y]) + " "
	print coluna


