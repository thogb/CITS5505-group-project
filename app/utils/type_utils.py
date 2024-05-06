# From https://stackoverflow.com/questions/715417/converting-from-a-string-to-boolean-in-python
# Date: 2024/06/05
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")
