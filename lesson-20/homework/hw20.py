import pandas as pd
import sqlite3

conn = sqlite3.connect("task/chinook.db")
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql_query("SELECT CustomerId, Total FROM invoices", conn)


customer_spent = (
    invoices.groupby("CustomerId")["Total"]
    .sum()
    .reset_index()
    .sort_values("Total", ascending=False)
)
top_customers = customer_spent.merge(customers, on="CustomerId")
top_5 = top_customers.head(5)[["CustomerId", "FirstName", "LastName", "Total"]]

print("🔹 Top 5 Customers by Total Purchase Amount:")
print(top_5)

invoice_items = pd.read_sql_query("SELECT InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", conn)
albums = pd.read_sql_query("SELECT AlbumId, Title FROM albums", conn)
invoice_to_customer = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM invoices", conn)

data = (
    invoice_items
    .merge(tracks, on="TrackId")
    .merge(invoice_to_customer, on="InvoiceId")
)
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().rename("TotalTracks")

customer_album_tracks = (
    data.groupby(["CustomerId", "AlbumId"])["TrackId"]
    .count()
    .reset_index(name="PurchasedTracks")
    .merge(album_track_counts, on="AlbumId")

customer_album_tracks["BoughtFullAlbum"] = (
    customer_album_tracks["PurchasedTracks"] == customer_album_tracks["TotalTracks"]
)
album_pref = (
    customer_album_tracks.groupby("CustomerId")["BoughtFullAlbum"]
    .any()
    .reset_index()
)

summary = album_pref["BoughtFullAlbum"].value_counts(normalize=True) * 100
summary = summary.rename(index={True: "Full Albums", False: "Individual Tracks"}).reset_index()
summary.columns = ["Purchase Type", "Percentage"]

print("\n🔹 Customer Purchase Preferences (Albums vs. Tracks):")
print(summary)

# Закрываем соединение
conn.close()
