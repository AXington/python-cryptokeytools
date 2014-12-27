from sshpubkeys import * # import errors

keys = [
 ["ssh-dss AAAAB3NzaC1kc3MAAACBAPlHIP5sD+T8/Sx1DGEiCzCXqpl7ww40jBg7wTkxu44OH6pNog5PjJt5M4NBULhKva/i+bhIM3ba+H1Or+aHWWFHACV6W2FCGk/k37ApRF8sIa4hsnN0P9qn6VfhbJKee+DBxa21WjjY/MZiljmJz7IQHx5RTxX9I/hJ7cL+aNmrAAAAFQCKteqc4IkgIrjpcpStsxYAhb3MqQAAAIEA+SfIKuTr7QPcinsZQDdmZOXqcg+u9TLzHA4c47y0Kns3T3BVPr9rWdmuh6eImzLO4wMLxLvcg3ecrqFuiCp1IHvXENkGlpB17S+uOXlVDY+sTdXyvYKRKirg5IZefIAP/m08c0QGkhFDbo4ysr9D5gXgH3LB2rMPIAbvMWm/HZQAAACBAKWtAE3hXRQX5KtI4AoIWVTly/6T4JNBt4u24ZRqV7X//CZEZ0cS5YpR/frlpUDI3WKoMtS+VmT3cBFZINashIxZyfBF8+0UX3s34HwNfp0hDW3ZdgZJU56GC2eclMantYGeVrMxgTQd80pxZFgByEhoXGeZaAwUzN8ULo9jHQo=", MalformedDataException, "too_short_data"],
 ["ssh-dss AAAAB3NzaC1kc3MAAACBAPlHIP5sD+T8/Sx1DGEiCzCXqpl7ww40jBg7wTkxu44OH6pNog5PjJt5M4NBULhKva/i+bhIM3ba+H1Or+aHWWFHACV6W2FCGk/k37ApRF8sIa4hsnN0P9qn6VfhbJKee+DBxa21WjjY/MZiljmJz7IQHx5RTxX9I/hJ7cL+aNmrAAAAFQCKteqc4IkgIrjpcpStsxYAhb3MqQAAAIEA+SfIKuTr7QPcinsZQDdmZOXqcg+u9TLzHA4c47y0Kns3T3BVPr9rWdmuh6eImzLO4wMLxLvcg3ecrqFuiCp1IHvXENkGlpB17S+uOXlVDY+sTdXyvYKRKirg5IZefIAP/m08c0QGkhFDbo4ysr9D5gXgH3LB2rMPIAbvMWm/HZQAAACBAKWtAE3hXRQX5KtI4AoIWVTly/6T4JNBt4u24ZRqV7X//CZEZ0cS5YpR/frlpUDI3WKoMtS+VmT3cBFZINashIxZyfBF8+0UX3s34HwNfp0hDW3ZdgZJU56GC2eclMantYGeVrMxgTQd80pxZFgByEhoXGeZaAwUzN8ULo9jHQqMjA==", MalformedDataException, "too_long_data"],
 ["ssh-dss AAAAB3NzaC1yc2EAAACBAPlHIP5sD+T8/Sx1DGEiCzCXqpl7ww40jBg7wTkxu44OH6pNog5PjJt5M4NBULhKva/i+bhIM3ba+H1Or+aHWWFHACV6W2FCGk/k37ApRF8sIa4hsnN0P9qn6VfhbJKee+DBxa21WjjY/MZiljmJz7IQHx5RTxX9I/hJ7cL+aNmrAAAAFQCKteqc4IkgIrjpcpStsxYAhb3MqQAAAIEA+SfIKuTr7QPcinsZQDdmZOXqcg+u9TLzHA4c47y0Kns3T3BVPr9rWdmuh6eImzLO4wMLxLvcg3ecrqFuiCp1IHvXENkGlpB17S+uOXlVDY+sTdXyvYKRKirg5IZefIAP/m08c0QGkhFDbo4ysr9D5gXgH3LB2rMPIAbvMWm/HZQAAACBAKWtAE3hXRQX5KtI4AoIWVTly/6T4JNBt4u24ZRqV7X//CZEZ0cS5YpR/frlpUDI3WKoMtS+VmT3cBFZINashIxZyfBF8+0UX3s34HwNfp0hDW3ZdgZJU56GC2eclMantYGeVrMxgTQd80pxZFgByEhoXGeZaAwUzN8ULo9jHQqM", InvalidTypeException, "key_type_mismatch"],
 ["ssh-dss AAAAB3NzaC1yc2EAAAADAQABAAAEAgDGrGaNv7i+sGSelzf+7JsCECa9a0sqSg8q4foGkjeV6RkS2tWvKXoT9rICjEdXXodj0CCVhe/V7dmAO0AK8KM0mcvPfTSC8zH1ZBsqaFFTWwmBD01fbH9axrrg3hM0f+AL4bMMWUdxdNrVo90s8PKU6k/HmUNLVx4gC6uQ4A6YczvOVZkuJ4f7HDYK/v1LNTRNeAkw94YpSIZVAoTOZN943+fRCE9cm155pwmFsS+wfzK9+jjhGXNEK0xooiVBRwQM7qetN076vV5FiiM0LO1qYi5JrIqK/70ske86x2mMhMkOe6jqQQbt32PFVmYqYJWcAYXz+bhcQw6oru0c6gNq53aGOnuqI0uh/zV2XH+cN4c8ABcOplzH5YQEUepNVzxylkvpWxdg/ZzR1pvyu5C8RkJWrE3AlCwpix1ak2xTDzgc3rwTTggNSYqvzmYq0mYJhZk2VWsLVxUgdxfwC3LvIHMXSTU9iU2Aqrlhy7bJAqxQFKWy05wsIOI6raPBLqZnPmJ76Ld9aXTrhBFfIDiigr9ZVsVAdOvmyAGCIj4x3Xnlol/3lN0M2+OSV1SU/5ZrS6dIlXPZDak/OXHU0iIFIODhYU5r8EI1M6BI/jsgQ8HatXmOJkfnIkVP0HxD1KvoAFKjVG5sM9KG12LqsnzfD1KL6PzxpOOgoVgznpOjSzVmPKAkU8N/r6R4VIAmZqxpF8Hlzqg/Gfh5kf6CJXXx8OQt1Z/DAsfnl3LvHFNuE8GgXgrUE022W9pV4oONgojc97JSgBXaFkK885UnJKTceAdGQvChEhsU1j3TiyKPox6ICGpoC2nGONJoDE8VQ8dE/YiZmqkZ1lJWX07EwevrIcnz1UBHFaR72aiAADRYClsitLA5+1mnydVstkQ8XQuuKNOFT7miaWUzRHwj9BYGb7oGhNd9oi1VTVjH/5Yq1UiHHESGaIjeLi5uG2KguDFpcvy2ngtUy3ZbvDj+DVOLL+3vAlycRPjN0nBE4e/J6UqdpLg0DbG56zNj86aU0ZgL8kL8NRkFHyV+5zG5iLFkGklbm4nwCxSW/bVT0PFD1is6JbtIk5i+liS+hiuzSF6NGouSuxDy95yWSG8/84fgPDFtvXtOD7Kl4P7EpEAL+VBZnremT9I8tRl1wOHxJKe7jbEcWC2zkuHNlju0Nv5SFijF9c+krRbHDYEzsxPpdqlI4gPtDFdkKwaKN6BrsxBsz9u+PhS1AloUYcxKRqWbqHuDBrKmxnhOgFqJ9ITX0RajtrApt1LfkSBXcFrVEx2nhQkGa6VwjcX/zw2I2iuJFOCQmc9udHIlyaCCSe1PqOIbOlOk5h/Gl1QvRNwSIgf9dZ05lZr6dc+VX8YGdyHsjQ==", InvalidTypeException, "rsa_key_no_match"],

 ["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAEAgDGrGaNv7i+sGSelzf+7JsCECa9a0sqSg8q4foGkjeV6RkS2tWvKXoT9rICjEdXXodj0CCVhe/V7dmAO0AK8KM0mcvPfTSC8zH1ZBsqaFFTWwmBD01fbH9axrrg3hM0f+AL4bMMWUdxdNrVo90s8PKU6k/HmUNLVx4gC6uQ4A6YczvOVZkuJ4f7HDYK/v1LNTRNeAkw94YpSIZVAoTOZN943+fRCE9cm155pwmFsS+wfzK9+jjhGXNEK0xooiVBRwQM7qetN076vV5FiiM0LO1qYi5JrIqK/70ske86x2mMhMkOe6jqQQbt32PFVmYqYJWcAYXz+bhcQw6oru0c6gNq53aGOnuqI0uh/zV2XH+cN4c8ABcOplzH5YQEUepNVzxylkvpWxdg/ZzR1pvyu5C8RkJWrE3AlCwpix1ak2xTDzgc3rwTTggNSYqvzmYq0mYJhZk2VWsLVxUgdxfwC3LvIHMXSTU9iU2Aqrlhy7bJAqxQFKWy05wsIOI6raPBLqZnPmJ76Ld9aXTrhBFfIDiigr9ZVsVAdOvmyAGCIj4x3Xnlol/3lN0M2+OSV1SU/5ZrS6dIlXPZDak/OXHU0iIFIODhYU5r8EI1M6BI/jsgQ8HatXmOJkfnIkVP0HxD1KvoAFKjVG5sM9KG12LqsnzfD1KL6PzxpOOgoVgznpOjSzVmPKAkU8N/r6R4VIAmZqxpF8Hlzqg/Gfh5kf6CJXXx8OQt1Z/DAsfnl3LvHFNuE8GgXgrUE022W9pV4oONgojc97JSgBXaFkK885UnJKTceAdGQvChEhsU1j3TiyKPox6ICGpoC2nGONJoDE8VQ8dE/YiZmqkZ1lJWX07EwevrIcnz1UBHFaR72aiAADRYClsitLA5+1mnydVstkQ8XQuuKNOFT7miaWUzRHwj9BYGb7oGhNd9oi1VTVjH/5Yq1UiHHESGaIjeLi5uG2KguDFpcvy2ngtUy3ZbvDj+DVOLL+3vAlycRPjN0nBE4e/J6UqdpLg0DbG56zNj86aU0ZgL8kL8NRkFHyV+5zG5iLFkGklbm4nwCxSW/bVT0PFD1is6JbtIk5i+liS+hiuzSF6NGouSuxDy95yWSG8/84fgPDFtvXtOD7Kl4P7EpEAL+VBZnremT9I8tRl1wOHxJKe7jbEcWC2zkuHNlju0Nv5SFijF9c+krRbHDYEzsxPpdqlI4gPtDFdkKwaKN6BrsxBsz9u+PhS1AloUYcxKRqWbqHuDBrKmxnhOgFqJ9ITX0RajtrApt1LfkSBXcFrVEx2nhQkGa6VwjcX/zw2I2iuJFOCQmc9udHIlyaCCSe1PqOIbOlOk5h/Gl1QvRNwSIgf9dZ05lZr6dc+VX8YGdyHsjQ=", InvalidKeyException, "broken_rsa_base64"],

 ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAH0GODBKRjsFB/1v3pDRGpA6xR+QpOJg9vat0brlbUNA=", TooShortKeyException, "too_short_ed25519"],
 ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIUGODBKRjsFB/1v3pDRGpA6xR+QpOJg9vat0brlbUNDDpA==", TooLongKeyException, "too_long_ed25519"],

 ["ecdsa-sha2-nistp255 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTUAAAAIbmlzdHAyNTUAAABBBE2gqbAChP2h3fTPx3Jy2KdOJUiBGEiqBUwoosfzllw+KrqmGiDEWlufSxdiSOFuLd4a8PSwhoWbdQRVFrZAvFE=", NotImplementedError, "invalid_nist_curve"],
 ["", InvalidKeyException, "empty_key"],
 ["- -", MalformedDataException, "no_content"],
 ["invalid-key-typeaaa AAAAE2ludmFsaWQta2V5LXR5cGVhYWEAAAAIbmlzdHAyNTUAAABBBE2gqbAChP2h3fTPx3Jy2KdOJUiBGEiqBUwoosfzllw+KrqmGiDEWlufSxdiSOFuLd4a8PSwhoWbdQRVFrZAvFE=", NotImplementedError, "not_implemented_key_type"],
]
