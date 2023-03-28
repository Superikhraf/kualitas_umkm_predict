from django.shortcuts import render

# our home page view
def home(request):
    return render(request, "index.html")


# custom method for generating predictions
def getPredictions(LB_IZINUSAHA, MK_BRANDING, DM_MEDSOS, KEU_LAPORAN, SDM_PELATIHAN):
    import pickle

    model = pickle.load(open("model\kualitas_ml_model.sav", "rb"))
    scaled = pickle.load(open("model\scaler.sav", "rb"))
    prediction = model.predict(
        scaled.transform([[LB_IZINUSAHA, MK_BRANDING, DM_MEDSOS, KEU_LAPORAN, SDM_PELATIHAN]])
    )

    if prediction == 0:
        return "Kualitas UMKM Perlu Ditingkatkan"
    elif prediction == 1:
        return "Kualitas UMKM-mu Bagus, Pertahankan"
    else:
        return "error"


# our result page view
def result(request):
    LB_IZINUSAHA = int(request.GET["LB_IZINUSAHA"])
    MK_BRANDING = int(request.GET["MK_BRANDING"])
    DM_MEDSOS = int(request.GET["DM_MEDSOS"])
    KEU_LAPORAN = int(request.GET["KEU_LAPORAN"])
    SDM_PELATIHAN = int(request.GET["SDM_PELATIHAN"])

    result = getPredictions(LB_IZINUSAHA, MK_BRANDING, DM_MEDSOS, KEU_LAPORAN, SDM_PELATIHAN)

    return render(request, "result.html", {"result": result})