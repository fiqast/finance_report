document.addEventListener("DOMContentLoaded", function () {
    const tipeTransaksiSelect = document.getElementById("tipeTransaksi");
    const kategoriSelect = document.getElementById("kategoriSelect");
    const kategoriKustomInput = document.getElementById("kategoriKustomInput");
    const jumlahInput = document.getElementById("jumlah");
    const submitButton = document.getElementById("submitButton");

    // Fungsi untuk memperbarui kategori berdasarkan tipe transaksi yang dipilih
    function updateCategoryOptions() {
        const tipeTransaksi = tipeTransaksiSelect.value;
        let kategoriOptions = [];

        // Reset kategori yang ada
        kategoriSelect.innerHTML = "<option value=''>Pilih Kategori</option>";

        // Menambahkan kategori berdasarkan tipe transaksi
        if (tipeTransaksi === "Pemasukan") {
            kategoriOptions = ["Cash", "Transfer Bank", "E-Wallet"];
        } else if (tipeTransaksi === "Pengeluaran") {
            kategoriOptions = ["Top Up E-Wallet", "Transfer Bank", "QRIS"];
        }

        // Menambahkan kategori ke dropdown
        kategoriOptions.forEach(function (kategori) {
            const option = document.createElement("option");
            option.value = kategori;
            option.textContent = kategori;
            kategoriSelect.appendChild(option);
        });

        // Menambahkan opsi untuk memilih kategori custom
        const customOption = document.createElement("option");
        customOption.value = "Kategori Custom";
        customOption.textContent = "Kategori Custom";
        kategoriSelect.appendChild(customOption);

        // Menampilkan input kategori custom jika ada
        toggleCustomCategoryInput();
    }

    // Fungsi untuk menampilkan atau menyembunyikan input kategori custom
    function toggleCustomCategoryInput() {
        if (kategoriSelect.value === "Kategori Custom") {
            kategoriKustomInput.style.display = "block";
        } else {
            kategoriKustomInput.style.display = "none";
            kategoriKustomInput.value = ""; // Reset nilai input custom
        }
    }

    // Fungsi untuk validasi input
    function validateForm() {
        const tipeTransaksi = tipeTransaksiSelect.value;
        const kategori = kategoriSelect.value;
        const jumlah = jumlahInput.value;

        if (!tipeTransaksi) {
            alert("Silakan pilih tipe transaksi.");
            return false;
        }
        if (!kategori) {
            alert("Silakan pilih kategori.");
            return false;
        }
        if (kategori === "Kategori Custom" && !kategoriKustomInput.value.trim()) {
            alert("Silakan isi kategori custom.");
            return false;
        }
        if (!jumlah || isNaN(jumlah) || jumlah <= 0) {
            alert("Silakan masukkan jumlah yang valid.");
            return false;
        }
        return true;
    }

    // Event listener untuk tipe transaksi
    tipeTransaksiSelect.addEventListener("change", updateCategoryOptions);

    // Event listener untuk kategori select
    kategoriSelect.addEventListener("change", toggleCustomCategoryInput);

    // Event listener untuk tombol submit
    submitButton.addEventListener("click", function (event) {
        if (!validateForm()) {
            event.preventDefault(); // Mencegah form submit jika validasi gagal
        }
    });

    // Memastikan kategori diupdate pada saat pertama kali halaman dimuat
    if (tipeTransaksiSelect.value) {
        updateCategoryOptions();
    }
});
