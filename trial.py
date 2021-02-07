# import json
# from downloader import download_data
#
# file = open('product_data.txt', 'a')
# link_file = open('link.txt', 'r')
# links = link_file.readlines()
# for link in links:
#     file = open('product_data.txt', 'a')
#     product = download_data(link)
#     file.write(json.dumps(product))
#     file.write('\n')
#     file.close()
# link_file.close()

x = list(range(1, 123))
print([y for y in x if (y%5==0) and (y%2==0)])
