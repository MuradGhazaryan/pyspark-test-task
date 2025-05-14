from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_categories(products, categories, product_categories):
    spark = SparkSession.builder.appName("ProductCategories").getOrCreate()
    product_cat_pairs = products.join(product_categories, "product_id", "left") \
                                .join(categories, "category_id", "left") \
                                .select(col("product_name"), col("category_name"))
    return product_cat_pairs