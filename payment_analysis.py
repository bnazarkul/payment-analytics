import pandas as pd

INPUT_FILE = "transactions.csv"
OUTPUT_FILE = "payment_analysis_results.xlsx"


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    return df


def calculate_kpis(df):
    successful = df[df["status"] == "Success"].copy()

    total_volume = successful["amount"].sum()
    total_commission = successful["commission"].sum()
    active_users = successful["user_id"].nunique()
    average_transaction = successful["amount"].mean()

    success_rate = (
        (df["status"] == "Success").sum() / len(df) * 100
        if len(df) > 0
        else 0
    )

    kpi_df = pd.DataFrame({
        "metric": [
            "Total Payment Volume",
            "Total Commission Revenue",
            "Active Users",
            "Average Transaction Amount",
            "Success Rate (%)",
        ],
        "value": [
            total_volume,
            total_commission,
            active_users,
            round(average_transaction, 2),
            round(success_rate, 2),
        ],
    })

    return successful, kpi_df


def category_analysis(successful):
    return (
        successful.groupby("category", as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            total_amount=("amount", "sum"),
            total_commission=("commission", "sum"),
            average_amount=("amount", "mean"),
        )
        .sort_values("total_amount", ascending=False)
    )


def daily_analysis(successful):
    return (
        successful.groupby("transaction_date", as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            daily_volume=("amount", "sum"),
            daily_commission=("commission", "sum"),
        )
        .sort_values("transaction_date")
    )


def user_analysis(successful):
    return (
        successful.groupby("user_id", as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            total_amount=("amount", "sum"),
        )
        .sort_values("total_amount", ascending=False)
    )


def save_results(kpis, categories, daily, users):
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        kpis.to_excel(writer, sheet_name="KPIs", index=False)
        categories.to_excel(writer, sheet_name="Categories", index=False)
        daily.to_excel(writer, sheet_name="Daily Dynamics", index=False)
        users.to_excel(writer, sheet_name="Top Users", index=False)


def main():
    print("Loading transaction data...")
    df = load_data(INPUT_FILE)

    print("Calculating KPIs...")
    successful, kpis = calculate_kpis(df)

    print("Building category analysis...")
    categories = category_analysis(successful)

    print("Building daily analysis...")
    daily = daily_analysis(successful)

    print("Building user analysis...")
    users = user_analysis(successful)

    print("Saving results...")
    save_results(kpis, categories, daily, users)

    print(f"Analysis completed: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
