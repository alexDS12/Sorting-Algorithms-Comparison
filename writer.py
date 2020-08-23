class Writer(object):

  def __init__(self, filename):
    self.filename = filename

  def write(self, content):
    with open(self.filename, 'a') as txt_file:
      txt_file.write(content + "\n")