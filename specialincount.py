def count_special_chars(filename):
      special_chars = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')
      dict_count = dict(zip(special_chars, [0] * len(special_chars)))

      with open(filename) as f:
          for passw in f:
              for c in passw:
                  if c in special_chars:
                      dict_count[c] += 1
      return dict_count
