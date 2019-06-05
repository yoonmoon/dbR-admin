



def setParameter(sql_str, parameter, value):
	try:
		val = int(value)
		return sql_str.replace("`{"+parameter.lower()+"}`", value)
	except ValueError:
		return sql_str.replace("`{"+parameter.lower()+"}`", "'"+value+"'")
