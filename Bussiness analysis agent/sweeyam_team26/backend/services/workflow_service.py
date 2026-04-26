from workflow.orchestrator import run_workflow


def run_analysis(orders_df, reviews_df, sellers_df, inventory_df):
    return run_workflow(
        orders_df,
        reviews_df,
        sellers_df,
        inventory_df
    )
