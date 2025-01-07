def test_dataset_samples():
    from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

    for domain, sample in VLMRUN_HUB_DATASET.items():
        assert sample.domain == domain, "Domain must match the sample domain"
        assert sample.prompt is not None, "Sample prompt must be present"
        assert sample.data is not None, "Sample data must be present"
        assert sample.response_model is not None, "Sample response model must be present"
