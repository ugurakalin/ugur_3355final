document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const ad = document.getElementById('ad').value;
    const soyad = document.getElementById('soyad').value;
    const email = document.getElementById('email').value;
    const sifre = document.getElementById('sifre').value;
    const sifreTekrar = document.getElementById('sifre-tekrar').value;
    const ulke = document.getElementById('ulke').value;
    const sehir = document.getElementById('sehir').value;

    if (sifre !== sifreTekrar) {
        alert('Sifreler eşleşmiyor.');
        return;
    }

    alert('Kayıt başarılı! LÜTFEN GİRİŞ SAYFASINA GİDİNİZ');


});