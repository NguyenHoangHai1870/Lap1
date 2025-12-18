# Lab 1 Report

BÁO CÁO THỰC HÀNH LAB 1: XÂY DỰNG TOKENIZER VÀ VECTORIZER

Môn học: Xử lý ngôn ngữ tự nhiên (NLP) Nội dung: Triển khai các thuật toán tách từ (Tokenization) và mô hình Túi từ (Bag of Words/CountVectorizer).



Cấu trúc thư mục dự án (Directory Structure)

├── data/                                # Thư mục chứa dữ liệu (Dataset)
│  
├── notebook/                            # Thư mục chứa Jupyter Notebooks (Mã nguồn chính)
│   ├── Lab1.pdf                         # Thực hành Tokenizer & Vectorizer
│   
├── report/                              # Thư mục chứa báo cáo
│   └── lap1.md                          # File báo cáo chi tiết này
│
├── src/                                 # Mã nguồn Python (Modules/Classes tái sử dụng)
│   └── Lap1
├── .gitignore                           # File cấu hình bỏ qua file rác (tmp, __pycache__)
└── README.md                            # Hướng dẫn chạy và tổng quan dự án


1. Các bước triển khai
Quá trình thực hiện bài Lab được chia thành 3 giai đoạn chính: Xây dựng kiến trúc (Interface), Cài đặt giải thuật, và Thử nghiệm.

Bước 1: Định nghĩa Interface (Abstract Base Classes)
Sử dụng thư viện abc của Python để định nghĩa khung sườn cho các lớp xử lý, đảm bảo tính nhất quán .


Class Tokenizer: Định nghĩa phương thức trừu tượng tokenize(text) nhận vào chuỗi và trả về danh sách các token (list of strings) .


Class Vectorizer: Định nghĩa các phương thức fit (học từ vựng từ corpus), transform (biến đổi văn bản thành vector), và fit_transform (kết hợp cả hai) .

Bước 2: Cài đặt các Tokenizer
Hai loại Tokenizer được cài đặt để so sánh hiệu quả xử lý:

RegrexTokenizer (Sử dụng biểu thức chính quy):

Chuyển văn bản về chữ thường.

Sử dụng re.findall(r"\w+|[^\w\s]", text) để tách các từ (word characters) và giữ lại các dấu câu không phải khoảng trắng.

SimpleTokenizer (Xử lý chuỗi cơ bản):

Sử dụng re.sub để chèn khoảng trắng xung quanh các dấu câu .,? giúp tách chúng ra khỏi từ dính liền.

Sử dụng phương thức .split() để tách chuỗi dựa trên khoảng trắng.

Bước 3: Cài đặt Vectorizer
CountVectorizer: Được kế thừa từ Vectorizer.


Phương thức fit: Duyệt qua toàn bộ văn bản trong tập dữ liệu (corpus), sử dụng tokenizer để tách từ, sau đó xây dựng bộ từ vựng (vocab) duy nhất và gán chỉ số (index) cho từng từ .

Phương thức transform: Tạo vector tần suất cho từng văn bản dựa trên bộ từ vựng đã học. Nếu từ xuất hiện, giá trị tại index tương ứng trong vector sẽ tăng lên .

2. Cách chạy code và ghi log kết quả
Môi trường và Dữ liệu

Môi trường: Google Colab.


Dữ liệu: File en_ewt-ud-train.txt (Dữ liệu văn bản tiếng Anh Universal Dependencies) được upload lên môi trường Colab .

Quy trình chạy và Ghi log
Code được chia thành các cell và chạy tuần tự. Kết quả được in ra màn hình console (Standard Output).

Task 1 & 2 (Kiểm thử Tokenizer):

Khởi tạo RegrexTokenizer và SimpleTokenizer.

Đưa vào danh sách các câu thử nghiệm chứa dấu câu, số và các trường hợp đặc biệt (ví dụ: "isn't", "123").

Sử dụng lệnh print để so sánh output của hai bộ tokenizer .

Task 3 (Thử nghiệm trên dữ liệu thực):

Đọc file en_ewt-ud-train.txt bằng hàm load_raw_text_data.

Lấy mẫu 500 ký tự đầu tiên và thực hiện tokenization.

Ghi log 20 token đầu tiên để kiểm tra .

Task 4 (Kiểm thử Vectorizer):

Tạo một corpus nhỏ gồm 3 câu: "I love NLP.", "I love programming.", "NLP is a subfield of AI.".

Chạy CountVectorizer để tạo bộ từ vựng và ma trận vector.

In vocab và ma trận kết quả .

3. Giải thích các kết quả thu được
Kết quả so sánh Tokenizer (Task 2)
Dựa trên log output , ta thấy sự khác biệt rõ rệt:

Xử lý dấu câu:

RegrexTokenizer: Tách rất kỹ, dấu câu được tách riêng hoàn toàn. Ví dụ: "Hello, world!" -> ['hello', ',', 'world', '!'] .

SimpleTokenizer: Cũng tách được dấu câu nhờ cơ chế chèn khoảng trắng (re.sub).

Xử lý từ viết tắt (Contractions - Ví dụ: "isn't", "Let's"):

Câu input: "NLP is fascinating... isn't it?"

RegrexTokenizer có xu hướng tách rời các thành phần ký tự đặc biệt. Ví dụ: "Let's" bị tách thành ['let', "'", 's'].

SimpleTokenizer giữ nguyên cụm "let's" hoặc "isn't" (tùy thuộc vào regex cụ thể trong re.sub chỉ xử lý .,?). Trong log, "Let's" được SimpleTokenizer giữ là ["let's"].

Kết quả trên dữ liệu thực (Task 3)
Đoạn văn bản mẫu: "American forces killed Shaikh Abdullah al-Ani...".

RegrexTokenizer: Tách cả dấu gạch ngang trong tên riêng. "al-zaman" -> ['al', '-', 'zaman'] (Log hiển thị: ['al', '', 'zaman'] do cách hiển thị list).

SimpleTokenizer: Giữ nguyên các từ nối bằng dấu gạch ngang nếu dấu này không nằm trong danh sách [.,?] cần tách. Kết quả là ['al-zaman'].

Kết quả Vectorization (Task 4)

Vocabulary: Bộ từ điển học được: {'a': 1, 'ai': 2, 'i': 3, 'is': 4, 'love': 5, 'nlp': 6...}.

Vector biểu diễn:

Câu 1 "I love NLP." (chứa 'i', 'love', 'nlp') -> Vector tương ứng có giá trị 1 tại các vị trí index 3, 5, 6. Kết quả log: [1, 0, 0, 1, 0, 1, 1...] (thứ tự khớp với vocab đã sort) .

Kết quả cho thấy thuật toán Bag of Words đã hoạt động đúng, đếm tần suất xuất hiện của từ trong câu dựa trên bộ từ vựng cố định.

4. Khó khăn gặp phải và Cách giải quyết
Trong quá trình thực hiện Lab 1, một số vấn đề kỹ thuật đã phát sinh:

Vấn đề: Xử lý các ký tự đặc biệt dính liền với từ (ví dụ: "world!", "test."). Nếu chỉ dùng hàm .split() thông thường, "world!" sẽ được coi là một từ riêng biệt khác với "world".


Giải quyết: Ở SimpleTokenizer, sử dụng Regular Expression re.sub(r"([.,?])", r" \1", text) để chèn khoảng trắng trước các dấu câu này, giúp hàm split() sau đó tách được từ và dấu câu riêng biệt.

Vấn đề: Sự khác biệt trong cách xử lý từ viết tắt (như "it's", "don't") giữa các phương pháp.

Giải quyết: Chấp nhận sự khác biệt do đặc thù thuật toán. RegrexTokenizer dùng mẫu \w+ nên sẽ cắt tại các ký tự không phải chữ cái (như dấu nháy đơn), trong khi SimpleTokenizer chỉ tách dựa trên khoảng trắng và một số dấu câu nhất định. Tùy vào bài toán thực tế sẽ chọn Tokenizer phù hợp.

Vấn đề: Xử lý File I/O trên Google Colab.


Giải quyết: Sử dụng google.colab.files.upload() để tải file thủ công từ máy local lên môi trường notebook .

5. Nguồn tham khảo và Model
Nguồn tham khảo:

Tài liệu hướng dẫn thực hành Lab 1 (được cung cấp trong file PDF).

Dữ liệu: Dataset UD_English-EWT (Universal Dependencies).

Thư viện Python: re (Regular Expression), abc (Abstract Base Class).

Mô hình sử dụng:

Bài thực hành này không sử dụng các Pre-trained Model (như BERT, GPT).

Toàn bộ các thuật toán Tokenizer và Vectorizer được cài đặt thủ công (from scratch) bằng Python thuần để hiểu rõ bản chất của phương pháp "Bag of Words" và xử lý chuỗi.
