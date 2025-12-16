
TRƯỜNG ĐẠI HỌC THỦ DẦU MỘT 
VIỆN CÔNG NGHỆ SỐ




CHUYÊN ĐỀ XỬ LÝ DỮ LIỆU LỚN

BÁO CÁO CUỐI KỲ
Đề tài:
Xây dựng Hệ thống Data Lakehouse & MLOps Cảnh báo  Thiên tai Thời gian thực (Case Study Tái hiện Siêu bão Yagi 2024)
				Nhóm: 16
Sinh viên thực hiện:
Lê Văn Hoàng	MSSV: 2224802010279
Nguyễn Văn Linh	MSSV: 2224802010841
Nguyễn Ngọc Hòa	MSSV: 2224802010935
Ngành: Công nghệ thông tin

Giáo viên hướng dẫn: TS. Nguyễn Hoàng Sỹ


Tp.HCM, Tháng 12 năm 2025 

TRƯỜNG ĐẠI HỌC THỦ DẦU MỘT 
VIỆN CÔNG NGHỆ SỐ


CHUYÊN ĐỀ XỬ LÝ DỮ LIỆU LỚN

BÁO CÁO CUỐI KỲ

Đề tài:
Xây dựng Hệ thống Data Lakehouse & MLOps Cảnh báo Thiên tai Thời gian thực (Case Study Tái hiện Siêu bão Yagi 2024)
				Nhóm: 16
Sinh viên thực hiện:
Lê Văn Hoàng	MSSV: 2224802010279
Nguyễn Văn Linh	MSSV: 2224802010841
Nguyễn Ngọc Hòa	MSSV: 2224802010935
Ngành: Công nghệ thông tin

Giáo viên hướng dẫn: TS. Nguyễn Hoàng Sỹ

Tp.HCM, Tháng 12 năm 2025 

KẾT QUẢ ĐÁNH GIÁ ĐỒ ÁN MÔN HỌC
Họ và tên giảng viên: TS. Nguyễn Hoàng Sỹ
Tên đề tài: Xây dựng Hệ thống Data Lakehouse & MLOps Cảnh báo Thiên tai Thời gian thực (Case Study Tái hiện Siêu bão Yagi 2024)
Họ tên SV1: Lê Văn Hoàng				MãSV1:2224802010279
Họ tên SV2: Nguyễn Văn Linh				MãSV2:2224802010841
Họ tên SV3: Nguyễn Ngọc Hòa				MãSV3:2224802010935
Nội dung	Trọng số	Điểm
1. Giải quyết vấn đề
1.1. Phân tích bài toán; thu thập, khảo sát và chuẩn bị dữ liệu; thiết kế giải thuật	20%	
1.2. Cài đặt, triển khai ứng dụng trên Hadoop	20%	
1.3. Cài đặt, triển khai ứng dụng trên Spark	20%	
2. Báo cáo bài tập lớn
2.1. Nội dung báo cáo	20%	
2.2. Vấn đáp	20%	
Điểm trung bình	
Giảng viên 

LỜI CẢM ƠN
Lời đầu tiên, nhóm chúng em xin gửi lời cảm ơn chân thành đến Thầy TS. Nguyễn Hoàng Sỹ đã tạo điều kiện thuận lợi, trang bị những kiến thức nền tảng quý báu cho chúng em trong suốt quá trình học tập và rèn luyện tại trường.
Thầy đã tận tình hướng dẫn, chỉ bảo và định hướng cho chúng em không chỉ về mặt lý thuyết các công nghệ Big Data hiện đại (như Kafka, Spark, Delta Lake) mà còn cả tư duy giải quyết bài toán thực tế. Sự hỗ trợ của Thầy là yếu tố then chốt giúp chúng em hoàn thành đồ án "Xây dựng Hệ thống Data Lakehouse & MLOps Cảnh báo Thiên tai Thời gian thực".
Thông qua đồ án này, đặc biệt là quá trình nghiên cứu case study về siêu bão Yagi, chúng em đã hiểu rõ hơn về tầm quan trọng của việc ứng dụng công nghệ trong công tác dự báo và giảm thiểu thiệt hại thiên tai.
Mặc dù đã rất cố gắng nỗ lực để hoàn thiện hệ thống pipeline xử lý dữ liệu từ thu thập đến cảnh báo, nhưng do giới hạn về mặt kiến thức và thời gian, đồ án khó tránh khỏi những thiếu sót. Chúng em rất mong nhận được những ý kiến đóng góp, nhận xét quý báu từ Quý Thầy để có thể hoàn thiện và phát triển đề tài tốt hơn trong tương lai.
Chúng em xin chân thành cảm ơn!
 
LỜI CAM ĐOAN
Nhóm chúng em xin cam đoan rằng toàn bộ nội dung trong báo cáo này là kết quả nghiên cứu, tìm hiểu và thực hiện của riêng em. Các tài liệu, số liệu và thông tin được sử dụng trong quá trình thực hiện đều được trích dẫn rõ ràng và trung thực theo đúng quy định. Chúng em hoàn toàn chịu trách nhiệm về tính chính xác, trung thực và nguyên bản của nội dung trong báo cáo này.
Nguyễn Văn Linh
Lê Văn Hoàng
Nguyễn Ngọc Hòa 
TÓM TẮT
Siêu bão Yagi (tháng 09/2024) đổ bộ vào Việt Nam đã gây ra những thiệt hại nghiêm trọng về người và tài sản, đặt ra yêu cầu cấp thiết về việc nâng cao năng lực cảnh báo sớm thiên tai. Tuy nhiên, các hệ thống phân tích dữ liệu truyền thống thường xử lý theo lô (batch processing) với độ trễ cao, khó đáp ứng được tốc độ dữ liệu từ các thiết bị IoT trong điều kiện thời tiết cực đoan.
Xuất phát từ thực tế đó, đồ án "Xây dựng Hệ thống Data Lakehouse & MLOps Cảnh báo Thiên tai Thời gian thực" được thực hiện nhằm giải quyết bài toán xử lý dữ liệu lớn với tốc độ cao. Nhóm nghiên cứu đề xuất và triển khai kiến trúc Lambda kết hợp Data Lakehouse, sử dụng các công nghệ lõi bao gồm: Apache Kafka (KRaft Mode) để thu thập dữ liệu streaming, Apache Spark để xử lý phân tích thời gian thực, và MinIO kết hợp Delta Lake để lưu trữ dữ liệu với tính năng ACID transactions.
Hệ thống tích hợp quy trình MLOps sử dụng thuật toán Random Forest (Scikit-learn) để phân tích các chỉ số khí tượng (tốc độ gió, áp suất, độ ẩm) và đưa ra cảnh báo nguy hiểm ngay lập tức.
Kết quả thực nghiệm tái hiện dữ liệu bão Yagi tại Hải Phòng (từ 05/09/2024 đến 09/09/2024) cho thấy hệ thống hoạt động ổn định với độ trễ xử lý dưới 1 giây, khả năng chịu lỗi (Fault Tolerance) tốt nhờ cơ chế tự phục hồi của Docker và đảm bảo tính nhất quán của dữ liệu. Đồ án đã chứng minh được tính khả thi của việc ứng dụng Big Data trong giám sát và cảnh báo thiên tai thời gian thực.
 
MỤC LỤC

LỜI CẢM ƠN	III
LỜI CAM ĐOAN	IV
TÓM TẮT	V
MỤC LỤC	VI
DANH MỤC HÌNH	IX
DANH MỤC BẢNG	XIII
CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI	1
1.1. Lý do chọn đề tài	1
1.1.1. Tính cấp thiết của vấn đề nghiên cứu	1
1.1.2. Hạn chế của các hệ thống phân tích truyền thống	2
1.1.3. Định hướng và giải pháp đề xuất.	3
1.2. Mục tiêu đề tài.	5
1.2.1. Mục tiêu tổng quát.	5
1.2.2. Mục tiêu cụ thể.	5
1.2.3. Ý nghĩa của mục tiêu nghiên cứu	6
1.3. Phạm vi nghiên cứu.	6
1.3.1. Phạm vi về dữ liệu.	6
1.3.2. Phạm vi về công nghệ	7
1.4. Cơ sở lý thuyết.	7
1.4.1. Tổng quan về big Data	7
1.5. Các kiến trúc big Data hiện đại.	9
1.5.1. Kiến trúc Batch Processing truyền thống.	9
1.5.2. Kiến trúc Stream Processing.	9
1.5.3. Lambda Architecture.	10
1.5.4. Kappa Architecture.	11
1.5.5. Kiến trúc Data Lakehouse.	12
1.6. Công nghệ sử dụng (Tech stack)	18
1.7. Các nghiên cứu liên quan (Related Works)	19
CHƯƠNG 2. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG	19
2.1. Kiến trúc tổng thể (Architecture)	19
2.1.1. Mô tả các lớp trong kiến trúc tổng thể.	19
2.1.3. Luồng dữ liệu tổng thể (Data Flow)	22
2.2. Thiết kế dữ liệu	22
2.3. Thiết kế kịch bản kiểm thử (Chaos Engineering)	23
CHƯƠNG 3. TRIỂN KHAI VÀ XÂY DỰNG	25
3.1. Chuẩn bị môi trường	25
3.2. Xây dựng Ingestion Layer (Sprint 2)	28
3.3. Xây dựng Processing & Storage Layer (Sprint 3)	28
3.4. Xây dựng MLOps Layer (Sprint 3)	29
3.5. Xây dựng Serving Layer (Sprint 4)	31
CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM	33
4.1. Kịch bản Demo: Tái hiện Bão Yagi	33
4.4. So sánh với lý thuyết	36
CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN	37
5.1. Kết luận.	37
5.2. Hạn chế của đề tài.	38
5.3. Hướng phát triển trong tương lai.	38
5.3.1. Tích hợp dữ liệu thời gian thực từ các nguồn thực tế	38
5.3.2. Triển khai hệ thống trên môi trường phân tán	39
5.3.3. Nâng cao mô hình Machine Learning và MLOps.	39
5.3.4. Mở rộng phạm vi ứng dụng.	39
TÀI LIỆU THAM KHẢO	40
 
DANH MỤC HÌNH
Hình 1.1.1: Hình ảnh cơn bão Yagi tiến vào Việt Nam.	1
Hình 1.5.3. Lambda Architecture	11
Hình 1.5.4. Kappa Architecture.	12
Hình 1.5.5.a.Delta Lake	14
Hình 1.5.5.b.ACID Transactions	15
Hình 1.5.5.c.Schema Enforcement	16
Hình 1.5.5.d.Time travel	16
Hình 2.1. Kiến trúc tổng thể (Architecture)	19
Hình 3.1.a.Cấu trúc thư mục dự án	25
Hình 3.1.b.Cấu hình file docker-compose	27
Hình 3.2. Đoạn mã yagi_producer.py	28
Hình 3.3. Đoạn mã spark_ingestion.py	29
Hình 3.4.a.Training Model	30
Hình 3.4.b. Đoạn mã predictor.py	31
Hình 3.5.Dashboard Streamlit	32
Hình 4.1.a.Khởi động hạ tầng	33
Hình 4.1.b.Kiểm tra services	34
Hình 4.1.c.Chạy Producer	35
Hình 4.1.d.Kết quả hiển thị mẫu	36

 
DANH MỤC BẢNG
Bảng 1.6. Công nghệ sử dụng	18
Bảng 2.2. Bảng chi tiết các trường dữ liệu	23
Bảng 2.3. Kịch bản kiểm thử	24

 

CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI

1.1. Lý do chọn đề tài
1.1.1. Tính cấp thiết của vấn đề nghiên cứu
Trong những năm gần đây, biến đổi khí hậu toàn cầu đang diễn ra ngày càng rõ rệt và phức tạp, kéo theo sự gia tăng cả về tần suất lẫn cường độ của các hiện tượng thời tiết cực đoan như bão mạnh, mưa lớn, lũ lụt và sạt lở đất. Những hiện tượng này đã và đang trở thành mối đe dọa nghiêm trọng đối với sự phát triển bền vững của nền kinh tế – xã hội, cũng như trực tiếp ảnh hưởng đến tính mạng và đời sống của người dân, đặc biệt tại các quốc gia ven biển như Việt Nam.
Một minh chứng điển hình cho thực trạng trên là siêu bão Yagi, đổ bộ vào Việt Nam vào tháng 09 năm 2024 [13]. Theo các số liệu thống kê và đánh giá chuyên môn, đây được ghi nhận là cơn bão mạnh nhất trong vòng 30 năm trở lại đây hướng vào Biển Đông, gây thiệt hại đặc biệt nghiêm trọng cho nhiều khu vực, trong đó chịu ảnh hưởng nặng nề nhất là các tỉnh ven biển như Hải Phòng và Quảng Ninh [14].
 
Hình 1.1.1: Hình ảnh cơn bão Yagi tiến vào Việt Nam.
Nguồn trích dẫn: https://vi.wikipedia.org/wiki/B%C3%A3o_Yagi_%282024%29
Sức tàn phá của siêu bão Yagi đã để lại những hậu quả nghiêm trọng cả về con người và kinh tế [14]. Cơn bão không chỉ gây ra hàng trăm trường hợp thiệt mạng và mất tích, mà còn làm thiệt hại kinh tế ước tính lên tới hàng chục nghìn tỷ đồng, đồng thời phá hủy nghiêm trọng hệ thống hạ tầng giao thông, lưới điện và thông tin liên lạc, gây gián đoạn lớn trong công tác cứu hộ, cứu nạn và khắc phục hậu quả sau thiên tai.
 
Nguồn tham khảo:  https://tienphong.vn/bao-yagi-manh-len-thanh-sieu-bao-trong-hom-nay-post1669853.tpo
Sự kiện siêu bão Yagi một lần nữa cho thấy những hạn chế của các phương thức giám sát và cảnh báo thiên tai truyền thống, đồng thời đặt ra yêu cầu cấp thiết phải xây dựng các hệ thống cảnh báo sớm hiện đại, có khả năng phân tích dữ liệu thời gian thực và đưa ra cảnh báo kịp thời. Việc nghiên cứu và ứng dụng các công nghệ tiên tiến như Big Data, xử lý dữ liệu streaming và trí tuệ nhân tạo vì thế trở thành một hướng tiếp cận cần thiết và có ý nghĩa thực tiễn cao trong bối cảnh hiện nay.
1.1.2. Hạn chế của các hệ thống phân tích truyền thống
Mặc dù trong những năm qua, Việt Nam đã từng bước đầu tư và triển khai nhiều hệ thống giám sát khí tượng – thủy văn nhằm phục vụ công tác dự báo và cảnh báo thiên tai, tuy nhiên các hệ thống hiện tại vẫn bộc lộ nhiều hạn chế, đặc biệt khi phải đối mặt với các hiện tượng thời tiết cực đoan có quy mô lớn và diễn biến nhanh như siêu bão Yagi.
Thứ nhất, phần lớn các hệ thống hiện nay vẫn dựa trên mô hình xử lý dữ liệu theo lô (Batch Processing). Dữ liệu khí tượng thường được thu thập, tổng hợp và phân tích theo chu kỳ cố định (theo giờ hoặc theo ngày), dẫn đến độ trễ cao trong việc phát hiện và phản ứng với các dấu hiệu nguy hiểm. Trong bối cảnh thiên tai diễn biến nhanh, độ trễ này có thể khiến các cảnh báo được đưa ra muộn, làm giảm đáng kể hiệu quả phòng ngừa và ứng phó.
Thứ hai, khả năng xử lý dữ liệu thời gian thực còn hạn chế. Khi xảy ra bão mạnh, lượng dữ liệu sinh ra từ các trạm quan trắc, cảm biến IoT, radar và vệ tinh tăng đột biến cả về số lượng lẫn tốc độ. Các hệ thống truyền thống gặp khó khăn trong việc tiếp nhận và xử lý khối lượng dữ liệu lớn với tốc độ cao, dẫn đến nguy cơ quá tải hệ thống, mất dữ liệu hoặc gián đoạn dịch vụ.
Thứ ba, khả năng mở rộng (Scalability) và tính chịu lỗi (Fault Tolerance) của các hệ thống hiện tại chưa đáp ứng yêu cầu thực tế. Nhiều hệ thống được thiết kế theo mô hình tập trung hoặc phụ thuộc vào hạ tầng cố định, khiến việc mở rộng khi có nhu cầu đột xuất trở nên phức tạp và tốn kém. Đồng thời, khi xảy ra sự cố phần cứng hoặc gián đoạn mạng, hệ thống có thể bị ngừng hoạt động, làm gián đoạn quá trình giám sát và cảnh báo.
Bên cạnh đó, việc tích hợp và khai thác dữ liệu lịch sử phục vụ phân tích nâng cao và huấn luyện mô hình dự báo còn hạn chế. Dữ liệu thường được lưu trữ rời rạc, thiếu tính nhất quán và không hỗ trợ các cơ chế đảm bảo toàn vẹn dữ liệu, gây khó khăn cho việc phân tích xu hướng dài hạn hoặc ứng dụng các mô hình Machine Learning.
Từ những hạn chế nêu trên có thể thấy rằng, các hệ thống giám sát và cảnh báo thiên tai hiện tại chưa đáp ứng đầy đủ yêu cầu về tính kịp thời, khả năng mở rộng và thông minh hóa trong bối cảnh biến đổi khí hậu ngày càng phức tạp. Điều này đặt ra yêu cầu cấp thiết phải nghiên cứu và xây dựng một kiến trúc hệ thống mới dựa trên các công nghệ Big Data hiện đại, có khả năng xử lý dữ liệu thời gian thực, lưu trữ dữ liệu quy mô lớn và hỗ trợ phân tích, dự báo thông minh.
1.1.3. Định hướng và giải pháp đề xuất.
Xuất phát từ những hạn chế của các hệ thống giám sát và cảnh báo thiên tai hiện tại, cùng với yêu cầu ngày càng cao về tính kịp thời, chính xác và khả năng mở rộng, đề tài định hướng nghiên cứu và xây dựng một hệ thống cảnh báo thiên tai thời gian thực dựa trên nền tảng Big Data hiện đại.
Cụ thể, đề tài đề xuất áp dụng kiến trúc Lambda Architecture [6][8] nhằm kết hợp hiệu quả giữa hai mô hình xử lý dữ liệu là xử lý thời gian thực (stream processing) và xử lý dữ liệu theo lô (batch processing) [7]. Kiến trúc này cho phép hệ thống vừa có khả năng phản ứng nhanh với các diễn biến bất thường của thiên tai, vừa đảm bảo lưu trữ đầy đủ dữ liệu lịch sử phục vụ phân tích chuyên sâu và huấn luyện mô hình dự báo.
Trong đó:
●	Lớp xử lý thời gian thực (Speed Layer): Đóng vai trò tiếp nhận và phân tích dữ liệu khí tượng ngay khi phát sinh từ các nguồn như cảm biến IoT hoặc dữ liệu mô phỏng, nhằm phát hiện sớm các chỉ số vượt ngưỡng nguy hiểm (ví dụ: tốc độ gió tăng đột biến, áp suất giảm mạnh).
●	Lớp xử lý theo lô (Batch Layer): Chịu trách nhiệm lưu trữ và xử lý toàn bộ dữ liệu lịch sử với độ chính xác cao, phục vụ phân tích xu hướng dài hạn, đánh giá hậu thiên tai và tái hiện diễn biến các sự kiện khí tượng lớn.
●	Lớp phục vụ (Serving Layer): Tổng hợp và cung cấp kết quả phân tích cho các hệ thống hiển thị và cảnh báo, đảm bảo thông tin được chuyển đến người dùng một cách kịp thời và nhất quán.
Bên cạnh đó, đề tài lựa chọn mô hình Data Lakehouse [9] làm nền tảng lưu trữ dữ liệu, kết hợp ưu điểm của Data Lake và Data Warehouse. Việc sử dụng MinIO [4] kết hợp với Delta Lake [3] giúp hệ thống đạt được khả năng lưu trữ dữ liệu quy mô lớn với chi phí thấp, đồng thời vẫn đảm bảo các đặc tính quan trọng như ACID Transactions, kiểm soát schema và khả năng truy vết dữ liệu theo thời gian.
Ngoài xử lý và lưu trữ dữ liệu, đề tài còn định hướng tích hợp Machine Learning và MLOps vào hệ thống nhằm nâng cao mức độ thông minh của quá trình cảnh báo. Thông qua việc huấn luyện và triển khai các mô hình dự báo trên dữ liệu khí tượng lịch sử, hệ thống có thể tự động đánh giá mức độ nguy hiểm của từng thời điểm, từ đó phát sinh cảnh báo một cách chủ động thay vì chỉ dựa trên các ngưỡng cố định.
Với cách tiếp cận trên, đề tài không chỉ hướng đến việc giải quyết bài toán cảnh báo thiên tai trong phạm vi nghiên cứu, mà còn đặt nền móng cho việc xây dựng các hệ thống giám sát và cảnh báo thông minh, có khả năng mở rộng và ứng dụng trong thực tế tại Việt Nam trong bối cảnh biến đổi khí hậu ngày càng nghiêm trọng.
1.2. Mục tiêu đề tài.
Xuất phát từ tính cấp thiết của bài toán cảnh báo thiên tai thời gian thực, cùng với những hạn chế còn tồn tại trong các hệ thống giám sát truyền thống, đề tài hướng tới việc nghiên cứu, thiết kế và triển khai một hệ thống Big Data hoàn chỉnh, có khả năng xử lý dữ liệu khí tượng quy mô lớn trong thời gian thực, phục vụ công tác giám sát và cảnh báo sớm thiên tai.
1.2.1. Mục tiêu tổng quát.
Mục tiêu tổng quát của đề tài là xây dựng và đánh giá một hệ thống Data Lakehouse kết hợp MLOps cho cảnh báo thiên tai thời gian thực, ứng dụng các công nghệ Big Data hiện đại nhằm tái hiện và phân tích diễn biến của siêu bão Yagi năm 2024. Thông qua đó, đề tài góp phần minh họa khả năng ứng dụng Big Data và trí tuệ nhân tạo trong các bài toán có ý nghĩa thực tiễn cao tại Việt Nam.
1.2.2. Mục tiêu cụ thể.
STT	Mục tiêu	Mô tả
1	Pipeline End-to-End	Xây dựng pipeline xử lý dữ liệu Streaming hoàn chỉnh từ thu thập đến hiển thị
2	Data Lakehouse	Triển khai kiến trúc lưu trữ hiện đại với MinIO + Delta Lake
3	MLOps	Ứng dụng Machine Learning để dự báo khí tượng thời gian thực
4	Data Replay	Tái hiện dữ liệu thực tế của bão Yagi tại Hải Phòng/Quảng Ninh
5	Fault Tolerance	Chứng minh khả năng tự phục hồi của hệ thống khi gặp sự cố
Bảng 1.2.2. Mục tiêu cụ thể
Để đạt được mục tiêu tổng quát nêu trên, đề tài tập trung vào các mục tiêu cụ thể sau:
●	Xây dựng pipeline xử lý dữ liệu end-to-end:
	Thiết kế và triển khai một pipeline xử lý dữ liệu streaming hoàn chỉnh, bắt đầu từ khâu thu thập dữ liệu khí tượng, truyền tải dữ liệu qua hệ thống message queue, xử lý thời gian thực, lưu trữ dữ liệu và hiển thị kết quả phân tích.
●	Triển khai kiến trúc Data Lakehouse:
	Áp dụng mô hình Data Lakehouse dựa trên MinIO và Delta Lake nhằm lưu trữ dữ liệu khí tượng với quy mô lớn, đảm bảo tính nhất quán, toàn vẹn dữ liệu và khả năng truy vết dữ liệu theo thời gian.
●	Ứng dụng MLOps trong dự báo và cảnh báo:
 	Nghiên cứu và triển khai quy trình huấn luyện, đóng gói và triển khai mô hình Machine Learning để đánh giá mức độ nguy hiểm của bão trong thời gian thực, từ đó hỗ trợ phát sinh cảnh báo tự động.
●	Tái hiện dữ liệu thực tế của siêu bão Yagi ( Data Relay):
	Sử dụng dữ liệu khí tượng lịch sử để mô phỏng lại diễn biến của siêu bão Yagi tại khu vực Hải Phòng và Quảng Ninh, qua đó kiểm chứng khả năng xử lý dữ liệu streaming và độ chính xác của hệ thống.
●	Đánh giá khả năng chịu lỗi và phục hồi của hệ thống (Fault Tolerance):
	Kiểm tra và chứng minh khả năng tự phục hồi (fault tolerance) của hệ thống khi xảy ra các sự cố như gián đoạn dịch vụ, quá tải dữ liệu hoặc lỗi thành phần, đảm bảo hệ thống vẫn hoạt động ổn định trong điều kiện khắc nghiệt.
1.2.3. Ý nghĩa của mục tiêu nghiên cứu
Việc đạt được các mục tiêu trên không chỉ giúp nhóm làm chủ các công nghệ Big Data cốt lõi như Apache Kafka [1], Apache Spark [2] và Data Lakehouse [9], mà còn góp phần:
●	Nâng cao khả năng ứng dụng kiến thức lý thuyết vào các bài toán thực tế
●	Minh họa vai trò của Big Data và Machine Learning trong lĩnh vực phòng chống thiên tai
●	Đặt nền móng cho các nghiên cứu và triển khai sâu hơn trong tương lai, hướng tới các hệ thống cảnh báo thiên tai thông minh, quy mô lớn.
1.3. Phạm vi nghiên cứu.
1.3.1. Phạm vi về dữ liệu.
Để đảm bảo tính thực tế cho bài toán tái hiện siêu bão Yagi, đề tài sử dụng nguồn dữ liệu khí tượng tin cậy từ Visual Crossing Weather Data. Phạm vi dữ liệu được giới hạn cụ thể như sau:
●	Thời gian: Dữ liệu được thu thập trong giai đoạn bão Yagi đổ bộ và gây ảnh hưởng mạnh nhất, kéo dài từ ngày 05/09/2024 đến ngày 09/09/2024.
●	Địa điểm: Tập trung phân tích tại khu vực Hải Phòng, Việt Nam – một trong những tâm điểm chịu thiệt hại nặng nề của cơn bão.
●	Các chỉ số phân tích: Hệ thống tập trung xử lý các trường dữ liệu quan trọng để dự báo thiên tai, bao gồm:
○	Tốc độ gió (windspeed)
○	Áp suất mực nước biển (sealevelpressure)
○	Nhiệt độ (temp)
○	Độ ẩm (humidity)
○	Lượng mưa (precip)
○	Độ che phủ mây (cloudcover).
1.3.2. Phạm vi về công nghệ
Hệ thống được xây dựng và triển khai dựa trên các công nghệ mã nguồn mở phổ biến trong hệ sinh thái Big Data và Data Science, bao gồm:
●	Apache Kafka [1]: Sử dụng làm hệ thống Message Queue để đệm và phân phối dữ liệu streaming.
●	Apache Spark Streaming [2]: Công cụ xử lý dữ liệu lớn thời gian thực (Real-time processing).
●	MinIO [4]: Hệ thống lưu trữ đối tượng (Object Storage) hiệu năng cao, đóng vai trò là Data Lake.
●	Docker [16]: Công nghệ container hóa dùng để đóng gói và triển khai môi trường.
●	Python [19] & Scikit-learn [18]: Ngôn ngữ lập trình chính để xây dựng pipeline và thư viện Machine Learning dùng cho module dự báo (Predictor).
1.4. Cơ sở lý thuyết.
1.4.1. Tổng quan về big Data
Trong kỷ nguyên số hóa, Big Data không chỉ đơn thuần là sự gia tăng về dung lượng lưu trữ mà còn là sự thay đổi căn bản trong cách thức thu thập, xử lý và khai thác giá trị từ dữ liệu [7]. Đối với bài toán cảnh báo thiên tai, đặc biệt là trường hợp của siêu bão Yagi, Big Data được định nghĩa và tiếp cận thông qua mô hình 3V đặc trưng:
1. Volume (Khối lượng dữ liệu): Đây là thách thức đầu tiên về mặt quy mô. Dữ liệu khí tượng trong hệ thống không chỉ là các con số đơn lẻ mà là một dòng chảy liên tục được thu thập từ hàng nghìn cảm biến IoT phân tán trên diện rộng. Các thiết bị này gửi dữ liệu với tần suất rất cao (theo từng phút hoặc từng giờ), tạo ra một khối lượng dữ liệu khổng lồ tích lũy theo thời gian, đòi hỏi hạ tầng lưu trữ phải có khả năng mở rộng linh hoạt.
2. Velocity (Tốc độ xử lý): Trong bối cảnh thiên tai, tốc độ chính là yếu tố sống còn. Hệ thống không thể chờ đợi dữ liệu được lưu trữ xong mới tiến hành phân tích. Yêu cầu đặt ra là phải xử lý thời gian thực (Real-time processing) với độ trễ cực thấp, lý tưởng là dưới 1 giây. Chỉ có tốc độ xử lý này mới đảm bảo các cảnh báo nguy hiểm được đưa ra kịp thời trước khi bão đổ bộ, giúp người dân và chính quyền có phương án ứng phó.
3. Variety (Sự đa dạng): Dữ liệu đầu vào của hệ thống không đồng nhất mà đến từ nhiều nguồn khác nhau bao gồm: các trạm quan trắc mặt đất (cảm biến), dữ liệu hình ảnh từ vệ tinh, và tín hiệu từ radar quét bão. Mỗi nguồn dữ liệu này lại có các định dạng cấu trúc khác nhau (JSON, Binary, CSV, Image...), đòi hỏi hệ thống phải có khả năng chuẩn hóa và tích hợp đa dạng các loại dữ liệu này vào một luồng xử lý thống nhất.
Tham khảo nguồn: [24]
Những thách thức trong Xử lý luồng (Stream Processing)
Việc áp dụng Big Data vào môi trường thời gian thực đặt ra những thách thức kỹ thuật phức tạp mà hệ thống Y.A.G.I cần giải quyết:
●	Đảm bảo tính nhất quán dữ liệu (Exactly-once semantics): Trong môi trường phân tán, việc gửi tin nhắn có thể bị lặp lại hoặc thất lạc. Hệ thống cần đảm bảo mỗi bản ghi dữ liệu chỉ được xử lý đúng một lần để tránh sai lệch trong kết quả dự báo.
●	Xử lý dữ liệu đến muộn (Late arriving data): Trong điều kiện bão lũ, đường truyền mạng thường không ổn định, dẫn đến việc dữ liệu từ cảm biến có thể đến server chậm hơn so với thời gian thực tế. Hệ thống cần cơ chế thông minh để sắp xếp và xử lý đúng thứ tự các dữ liệu này thay vì loại bỏ chúng.
●	Kỹ thuật Cửa sổ trượt (Sliding window): Để dự báo xu hướng bão, không thể chỉ nhìn vào một điểm dữ liệu tại một thời điểm. Hệ thống cần áp dụng kỹ thuật cửa sổ trượt (ví dụ: xét dữ liệu trong 15 phút gần nhất) để phân tích sự thay đổi của tốc độ gió và áp suất, từ đó nhận diện chính xác xu hướng mạnh lên hay yếu đi của cơn bão.
1.5. Các kiến trúc big Data hiện đại.
Trong bối cảnh dữ liệu ngày càng gia tăng cả về khối lượng, tốc độ và mức độ đa dạng, các kiến trúc Big Data truyền thống dần bộc lộ nhiều hạn chế, đặc biệt là trong các bài toán yêu cầu xử lý dữ liệu thời gian thực và khả năng mở rộng cao. Do đó, nhiều kiến trúc Big Data hiện đại đã được đề xuất và ứng dụng rộng rãi nhằm đáp ứng các yêu cầu mới về hiệu năng, độ tin cậy và tính linh hoạt của hệ thống.
1.5.1. Kiến trúc Batch Processing truyền thống [7].
Kiến trúc Batch Processing là mô hình xử lý dữ liệu theo từng lô (batch), trong đó dữ liệu được thu thập trong một khoảng thời gian nhất định trước khi đưa vào xử lý. Mô hình này thường được triển khai với các hệ thống như Hadoop MapReduce.
Ưu điểm:
●	Phù hợp với xử lý dữ liệu lịch sử quy mô lớn
●	Dễ triển khai và quản lý
●	Độ chính xác cao do xử lý toàn bộ dữ liệu
Hạn chế:
●	Độ trễ xử lý cao
●	Không phù hợp với các bài toán yêu cầu phản hồi nhanh
●	Không đáp ứng được yêu cầu cảnh báo thời gian thực
Trong bối cảnh cảnh báo thiên tai, kiến trúc này không thể phát hiện kịp thời các diễn biến nguy hiểm do thời gian xử lý kéo dài.
1.5.2. Kiến trúc Stream Processing [7].
Kiến trúc Stream Processing tập trung vào việc xử lý dữ liệu ngay khi dữ liệu được sinh ra. Các framework phổ biến cho mô hình này bao gồm Apache Storm, Apache Flink và Apache Spark Structured Streaming.
Ưu điểm:
●	Độ trễ thấp, gần thời gian thực
●	Phù hợp với các hệ thống giám sát và cảnh báo
●	Khả năng mở rộng tốt
Hạn chế:
●	Khó xử lý dữ liệu lịch sử phức tạp
●	Việc replay và hiệu chỉnh dữ liệu gặp nhiều khó khăn
●	Đòi hỏi hệ thống ổn định và cấu hình phức tạp
Mặc dù phù hợp với cảnh báo sớm, nhưng nếu chỉ sử dụng Stream Processing thì hệ thống sẽ gặp hạn chế trong việc phân tích dài hạn và huấn luyện mô hình Machine Learning.
Tham khảo nguồn [25]
1.5.3. Lambda Architecture [6][8].
Lambda Architecture là một kiến trúc xuất sắc để xử lý dữ liệu thời gian thực và xây dựng các hệ thống chịu lỗi, có khả năng mở rộng, là một trong những kiến trúc Big Data hiện đại và phổ biến nhất. Ngoài việc được thiết kế nhằm kết hợp ưu điểm của cả Batch Processing và Stream Processing, kiến trúc Lamda còn bao gồm một lớp phục vụ dữ liệu để phản hồi các truy vấn của người dùng.
Có 2 cách tiếp cận đối với kiến trúc Lamda:
●	Hybird Approach: Tiếp cận hỗn hợp.
Nó được thiết kế để khai thác khối lượng dữ liệu khổng lồ được tạo ra nhanh chóng, cho phép các doanh nghiệp sử dụng dữ liệu nhanh hơn.
●	Speciffic Approach: Tiếp cận cụ thể.
Nó cố gắng cân bằng độ trễ, thông lượng và khả năng chịu lỗi bằng cách sử dụng xử lý theo lô để cung cấp cái nhìn chính xác từ dữ liệu theo lô, trong khi đồng thời sử dụng xử lý luồng thời gian thực để cung cấp cái nhìn về dữ liệu trực tuyến. Các đầu ra từ cả 2 lớp theo lô và tốc độ có thể được hợp nhất trước khi trình bày.
 
Hình 1.5.3. Lambda Architecture
Kiến trúc này chủ yếu có 3 lớp để xử lý dữ liệu lớn:
●	Batch Layer: Lưu trữ toàn bộ dữ liệu gốc và xử lý dữ liệu lịch sử
●	Speed Layer: Xử lý dữ liệu mới phát sinh với độ trễ thấp
●	Serving Layer: Cung cấp kết quả xử lý cho các ứng dụng
Ưu điểm:
●	Kết hợp xử lý thời gian thực và xử lý dữ liệu lịch sử
●	Đảm bảo độ chính xác và tính kịp thời
●	Hỗ trợ tốt cho các bài toán phân tích và Machine Learning
Hạn chế:
●	Kiến trúc phức tạp
●	Phải duy trì hai pipeline xử lý song song
Trong đề tài này, Lambda Architecture được lựa chọn vì đáp ứng đồng thời yêu cầu cảnh báo thời gian thực và tái hiện diễn biến của siêu bão Yagi.
1.5.4. Kappa Architecture [7]. 
Kiến trúc Kappa là một phương pháp thiết kế hệ thống tinh gọn tập trung vào xử lý dữ liệu theo thời gian thực [7]. Khác với kiến trúc Lamda, xử lý cả dữ liệu lô và dữ liệu theo thời gian thực, Kappa loại bỏ nhu cầu về một lớp lô, đơn giản hóa kiến trúc. Bằng cách xử lý tất cả dữ liệu như một luồng, nó cung cấp khả năng mở rộng, độ trễ thấp hơn và bảo trì dễ dàng hơn. Thiết kế này đặc biệt phù hợp cho các ứng dụng yêu cầu phân tích theo thời gian thực, hệ thống dựa trên sự kiện và tích hợp dữ liệu liên tục.
Ưu điểm:
●	Kiến trúc đơn giản
●	Dễ bảo trì
●	Giảm chi phí vận hành
Hạn chế:
●	Khó xử lý các tác vụ batch phức tạp
●	Việc replay dữ liệu phụ thuộc nhiều vào hệ thống streaming
●	Không tối ưu cho các bài toán cần phân tích lịch sử sâu
 
Hình 1.5.4. Kappa Architecture. 
1.5.5. Kiến trúc Data Lakehouse [9].
Data Lakehouse là kiến trúc lưu trữ dữ liệu hiện đại, được xây dựng nhằm kết hợp những ưu điểm nổi bật của Data Lake và Data Warehouse, đồng thời khắc phục các hạn chế vốn có của từng mô hình riêng lẻ [9]. Thay vì tách biệt hệ thống lưu trữ dữ liệu thô và hệ thống phân tích, Data Lakehouse cho phép lưu trữ, quản lý và phân tích dữ liệu trên cùng một nền tảng thống nhất.
Data Lakehouse được triển khai thông qua sự kết hợp giữa:
●	Data Lake (MinIO): đảm nhiệm vai trò lưu trữ dữ liệu thô với quy mô lớn
●	Data Warehouse layer (Delta Lake): cung cấp các cơ chế quản lý dữ liệu nâng cao như ACID Transactions, Schema Enforcement và Time Travel
Vai trò của Data Lake trong kiến trúc Lakehouse (MinIO)
Trong kiến trúc Data Lakehouse, MinIO [4] được sử dụng như một nền tảng object storage tương thích chuẩn S3, đóng vai trò là Data Lake.
MinIO cho phép:
●	Lưu trữ dữ liệu ở dạng thô (raw data) ngay khi được sinh ra từ các nguồn streaming
●	Hỗ trợ đa định dạng dữ liệu như CSV, JSON, Parquet, log hoặc dữ liệu bán cấu trúc
●	Mở rộng linh hoạt và chi phí thấp so với các hệ thống lưu trữ truyền thống
Việc lưu trữ dữ liệu thô trong MinIO giúp hệ thống giữ lại toàn bộ dữ liệu gốc, phục vụ cho việc tái hiện dữ liệu, phân tích lịch sử và huấn luyện lại mô hình Machine Learning khi cần thiết.
Vai trò của Data Warehouse layer trong Lakehouse (Delta Lake)
Mặc dù Data Lake có khả năng lưu trữ mạnh mẽ, nhưng bản thân nó thiếu các cơ chế quản lý dữ liệu cần thiết cho phân tích và vận hành hệ thống. Do đó, Delta Lake [3] được sử dụng như một lớp Data Warehouse đặt lên trên Data Lake.
 
Hình 1.5.5.Delta Lake
Delta Lake [3] cung cấp các đặc tính quan trọng:
●	ACID Transactions
		Delta Lake đảm bảo các thao tác ghi và đọc dữ liệu diễn ra một cách nhất quán, an toàn và đáng tin cậy, ngay cả khi có nhiều tiến trình xử lý dữ liệu đồng thời. Điều này đặc biệt quan trọng trong các hệ thống streaming, nơi dữ liệu liên tục được ghi vào Data Lake.
 
Hình 1.5.5.ACID Transactions
●	Schema Enforcement
		Delta Lake cho phép kiểm soát và áp đặt schema dữ liệu, giúp phát hiện sớm các bản ghi không hợp lệ và tránh việc dữ liệu bị sai cấu trúc. Nhờ đó, chất lượng dữ liệu trong hệ thống được đảm bảo tốt hơn so với Data Lake truyền thống.
 
Hình 1.5.5.Schema Enforcement
●	Time Travel
		Một trong những đặc điểm nổi bật của Delta Lake là khả năng truy vết dữ liệu theo thời gian, cho phép truy vấn lại dữ liệu tại một thời điểm hoặc phiên bản bất kỳ. Tính năng này đặc biệt hữu ích trong các bài toán Machine Learning và phân tích thiên tai, khi cần so sánh dữ liệu giữa các giai đoạn khác nhau hoặc tái hiện lại diễn biến của một sự kiện trong quá khứ.
 
Hình 1.5.5. Time travel
Nguồn tham khảo: [26]


Ưu điểm của kiến trúc Data Lakehouse
Việc kết hợp MinIO và Delta Lake trong kiến trúc Data Lakehouse mang lại nhiều lợi ích vượt trội:
●	Thống nhất lưu trữ và phân tích: dữ liệu chỉ cần lưu một lần nhưng có thể phục vụ nhiều mục đích khácthống.
●	Hỗ trợ xử lý thời gian thực và batch: phù hợp với kiến trúc Lambda Architethống.
●	Nền tảng lý tưởng cho Machine Learning và MLOps: dữ liệu lịch sử và dữ liệu streaming cùng tồn tại trên một hệ thống.
●	Khả năng mở rộng cao: dễ dàng mở rộng khi khối lượng dữ liệu tăng đột biến trong các tình huống thiên tai.
 

1.6. Công nghệ sử dụng (Tech stack)

Thành phần	Công nghệ	Phiên bản	Vai trò
Message Queue	Apache Kafka [1]	KRaft Mode	Pub/Sub, Buffer, Decoupling
Processing	Apache Spark [2]	3.5.3	Stream Processing, ETL
Storage	MinIO [4]	Latest	Object Storage (S3 Compatible)
Data Format	Delta Lake [3]	3.1.0	ACID, Time Travel, Schema
Container	Docker Compose	v2+	Orchestration, Isolation
Monitoring	Portainer	CE Latest	Container Management
ML Framework	Scikit-learn	1.x	Model Training
Language	Python	3.9+	PySpark, Producer, Predictor
Bảng 1.6. Công nghệ sử dụng

1.7. Các nghiên cứu liên quan (Related Works)
Trong phần này, nhóm nghiên cứu trình bày tổng quan các công trình khoa học đã được công bố, có liên quan trực tiếp đến các thành phần kỹ thuật và phương pháp tiếp cận được sử dụng trong đề tài. Việc khảo sát các nghiên cứu liên quan giúp định vị đề tài trong bối cảnh học thuật, đồng thời làm rõ những điểm kế thừa và đóng góp mới của nhóm.

1.7.1. Nghiên cứu về xử lý dữ liệu thời gian thực trong dự báo thời tiết
Một trong những nghiên cứu tiêu biểu trong lĩnh vực này là công trình "Weather Prediction Model using Random Forest Algorithm and Apache Spark" [10]. Nghiên cứu này đề xuất một mô hình dự báo thời tiết sử dụng Apache Kafka để thu thập dữ liệu streaming, Apache Spark để xử lý phân tích, và thuật toán Random Forest để dự báo các chỉ số khí tượng. Kết quả cho thấy hệ thống có khả năng xử lý dữ liệu với độ trễ thấp và đạt độ chính xác cao trong dự báo.

Đề tài của nhóm kế thừa kiến trúc tổng thể từ nghiên cứu này (Kafka + Spark + Random Forest), đồng thời bổ sung thêm lớp Data Lakehouse để lưu trữ dữ liệu lịch sử phục vụ phân tích dài hạn.

1.7.2. Nghiên cứu về kiến trúc Lambda trong hệ thống Big Data
Nghiên cứu "Lambda Architecture for Real Time Big Data Analytic" của Dimovski và cộng sự [11] đã chứng minh tính hiệu quả của việc áp dụng Lambda Architecture trong các hệ thống phân tích dữ liệu lớn thời gian thực. Các tác giả trình bày chi tiết cách kết hợp Batch Layer và Speed Layer để đạt được cả độ chính xác cao (từ batch processing) và độ trễ thấp (từ stream processing).

Đề tài của nhóm áp dụng nguyên lý tương tự, với Speed Layer (Predictor) xử lý cảnh báo tức thời và Batch Layer (Spark + Delta Lake) lưu trữ dữ liệu trong Data Lakehouse phục vụ phân tích lịch sử.

Ngoài ra, nghiên cứu "Strategies for Big Data Analytics through Lambda Architectures in Volatile Environments" [12] cũng cung cấp các chiến lược để triển khai Lambda Architecture trong môi trường biến động, phù hợp với bối cảnh thiên tai của đề tài.

1.7.3. Nghiên cứu về kiến trúc Data Lakehouse
Khái niệm Data Lakehouse được giới thiệu chính thức trong bài báo "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics" của Armbrust và cộng sự (Databricks, 2021) [9]. Nghiên cứu này chỉ ra rằng việc kết hợp tính linh hoạt của Data Lake với khả năng quản lý dữ liệu của Data Warehouse thông qua các table format như Delta Lake giúp giải quyết vấn đề "data swamp" và cải thiện hiệu năng truy vấn.

Đề tài của nhóm triển khai kiến trúc Data Lakehouse sử dụng MinIO làm Object Storage và Delta Lake làm table format, đảm bảo các đặc tính ACID và Time Travel cho dữ liệu khí tượng.

1.7.4. So sánh với các nghiên cứu liên quan

Tiêu chí	Weather Prediction [10]	Lambda Architecture [11]	Đề tài Y.A.G.I (2024)
Kiến trúc	Kappa (Stream only)	Lambda	Lambda + Data Lakehouse
Message Queue	Apache Kafka	Apache Kafka	Apache Kafka (KRaft Mode)
Processing Engine	Apache Spark	Spark/Storm	Spark Structured Streaming
Storage	Không đề cập	HDFS/Cassandra	MinIO + Delta Lake
ML Model	Random Forest	Không có	Random Forest (Scikit-learn)
Bài toán	Dự báo thời tiết	Phân tích Big Data	Cảnh báo bão thời gian thực
Triển khai	Cluster	Cluster	Docker Compose (Single Node)

Bảng 1.7. So sánh với các nghiên cứu liên quan

1.7.5. Đóng góp của đề tài
So với các nghiên cứu liên quan, đề tài của nhóm có những đóng góp và điểm khác biệt sau:

●	Tích hợp Data Lakehouse: Trong khi các nghiên cứu trước chủ yếu sử dụng HDFS hoặc các hệ thống lưu trữ truyền thống, đề tài này là một trong những nỗ lực đầu tiên kết hợp MinIO và Delta Lake vào pipeline xử lý dữ liệu khí tượng, mang lại các lợi ích về ACID transactions và Time Travel.
●	Tối ưu cho môi trường tài nguyên hạn chế: Các nghiên cứu trước thường triển khai trên cluster quy mô lớn. Đề tài này chứng minh tính khả thi của việc triển khai hệ thống Big Data hoàn chỉnh trên máy tính cá nhân (16GB RAM) thông qua Docker Compose và Kafka KRaft Mode.
●	Case Study thực tế tại Việt Nam: Sử dụng dữ liệu siêu bão Yagi (2024) tại Hải Phòng làm case study, đề tài mang tính ứng dụng cao và phù hợp với bối cảnh thiên tai tại Việt Nam.
●	Quy trình MLOps đơn giản hóa: Thay vì sử dụng các mô hình Deep Learning phức tạp, đề tài áp dụng Random Forest kết hợp với quy trình đóng gói Docker, giúp dễ dàng triển khai và bảo trì trong môi trường production.
CHƯƠNG 2. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
2.1. Kiến trúc tổng thể (Architecture)
 
Hình 2.1. Kiến trúc tổng thể (Architecture) 
Hệ thống cảnh báo thiên tai trong đề tài được thiết kế dựa trên Lambda Architecture [6][8], kết hợp với mô hình Data Lakehouse [9], nhằm đáp ứng đồng thời các yêu cầu về xử lý dữ liệu thời gian thực, lưu trữ dữ liệu lịch sử quy mô lớn và tích hợp Machine Learning cho bài toán dự báo thiên tai.
Kiến trúc tổng thể của hệ thống được xây dựng theo hướng end-to-end, cho phép dữ liệu được xử lý liên tục từ khâu thu thập, xử lý, lưu trữ cho đến hiển thị và phát sinh cảnh báo. Toàn bộ hệ thống được chia thành các lớp chức năng rõ ràng, đảm bảo tính mở rộng, khả năng chịu lỗi và dễ dàng bảo trì.
2.1.1. Mô tả các lớp trong kiến trúc tổng thể.
1. Data Source - Nguồn dữ liệu
Nguồn dữ liệu đầu vào của hệ thống là dữ liệu khí tượng liên quan đến siêu bão Yagi (09/2024), được thu thập từ nền tảng Visual Crossing Weather. Dữ liệu được lưu trữ dưới dạng file CSV, bao gồm các chỉ số khí tượng quan trọng như:
●	Tốc độ gió
●	Áp suất khí quyển
●	Nhiệt độ
●	Độ ẩm
●	Lượng mưa
●	Độ che phủ mây
Dữ liệu lịch sử này được sử dụng để tái hiện (data replay) kịch bản dòng dữ liệu thời gian thực, giúp mô phỏng điều kiện vận hành của một hệ thống cảnh báo thiên tai trong thực tế.
2. Ingestion Layer - Lớp thu thập dữ liệu
Lớp Ingestion chịu trách nhiệm tiếp nhận dữ liệu từ nguồn và đưa vào hệ thống xử lý streaming. Trong kiến trúc này, Apache Kafka [1] đóng vai trò là nền tảng message queue trung tâm.
Một Python Producer đọc dữ liệu từ file CSV và gửi từng bản ghi vào Kafka topic weather-stream. Quá trình này giúp biến dữ liệu lịch sử thành luồng dữ liệu streaming, mô phỏng dữ liệu khí tượng phát sinh liên tục theo thời gian.
Kafka đảm bảo:
●	Không mất dữ liệu (durability)
●	Khả năng mở rộng cao
●	Hỗ trợ nhiều consumer hoạt động song song
●	Cho phép replay dữ liệu khi cần thiết
3. Process Layer - Lớp xử lý dữ liệu
Lớp Process là trái tim của pipeline, nơi dữ liệu được xử lý và phân tích theo thời gian thực. Thành phần chính tại lớp này là Apache Spark Streaming [2].
Spark Streaming đóng vai trò consumer của Kafka, thực hiện các nhiệm vụ:
●	Parse dữ liệu JSON
●	Kiểm tra và validate schema
●	Chuẩn hóa dữ liệu
●	Tính toán các chỉ số tổng hợp
●	Phát hiện các điều kiện vượt ngưỡng nguy hiểm
Spark được triển khai theo mô hình Master – Worker, cho phép xử lý song song trên nhiều node, đảm bảo hiệu năng và khả năng mở rộng khi khối lượng dữ liệu tăng cao.
4. Storage & Intelligence Layer - Lớp lưu trữ và trí tuệ dữ liệu
Lớp Storage & Intelligence được triển khai theo mô hình Data Lakehouse [9], kết hợp ưu điểm của Data Lake và Data Warehouse.
●	MinIO [4] đóng vai trò Data Lake, lưu trữ dữ liệu thô và dữ liệu đã xử lý với chi phí thấp.
●	Delta Lake [3] cung cấp các tính năng nâng cao như:
○	ACID Transactions
○	Schema Enforcement
○	Time Travel
Dữ liệu lịch sử được lưu trữ tại đây phục vụ:
●	Phân tích xu hướng khí tượng
●	Huấn luyện mô hình Machine Learning
●	Đánh giá lại các sự kiện thiên tai đã xảy ra
Ngoài ra, các mô hình dự báo được huấn luyện và triển khai theo hướng MLOps, sau đó được đóng gói trong Docker để phục vụ suy luận (inference) trên dữ liệu streaming.
5. Serving Layer - Lớp phục vụ và hiển thị
Lớp Serving chịu trách nhiệm hiển thị kết quả và phát sinh cảnh báo. Trong hệ thống này:
●	Streamlit được sử dụng để xây dựng dashboard hiển thị dữ liệu thời gian thực và dữ liệu lịch sử
●	Các biểu đồ về gió, áp suất, lượng mưa được cập nhật liên tục
●	Các cảnh báo nguy hiểm được hiển thị ngay khi mô hình dự báo phát hiện rủi ro
Bên cạnh đó, Portainer được sử dụng để giám sát và quản lý các container Docker, hỗ trợ vận hành và theo dõi trạng thái hệ thống.
2.1.3. Luồng dữ liệu tổng thể (Data Flow)
Luồng dữ liệu trong hệ thống được mô tả theo các bước sau:
1.	Dữ liệu khí tượng được lưu trữ dưới dạng file CSV
2.	Python Producer đọc dữ liệu và gửi từng record vào Kafka topic weather-stream
3.	Kafka phân phối dữ liệu cho các consumer
4.	Spark Streaming xử lý dữ liệu thời gian thực và ghi dữ liệu lịch sử vào Delta Lake trên MinIO
5.	Dịch vụ ML Predictor thực hiện inference và phân loại mức độ nguy hiểm
6.	Các cảnh báo được gửi vào Kafka topic storm-alerts
7.	Dashboard Streamlit đọc dữ liệu và hiển thị biểu đồ thời gian thực cùng cảnh báo
Luồng dữ liệu này đảm bảo hệ thống vừa có khả năng phản ứng nhanh với các sự kiện nguy hiểm, vừa lưu trữ đầy đủ dữ liệu lịch sử để phục vụ phân tích và huấn luyện mô hình.
2.2. Thiết kế dữ liệu
1. Schema nguồn dữ liệu (Input)
Hệ thống sử dụng dữ liệu đầu vào mô phỏng các bản tin khí tượng dưới dạng file CSV. Cấu trúc dữ liệu chi tiết như sau:
●	Đường dẫn file: data/yagi_storm.csv
●	Quy mô mẫu: 120 bản ghi (tương ứng với dữ liệu của 5 ngày, mỗi ngày 24 giờ)
●	Tần suất dữ liệu: 1 bản ghi/giờ
Bảng chi tiết các trường dữ liệu:
Tên trường (Cột)	Kiểu dữ liệu	Mô tả ý nghĩa
name	String	Tên địa điểm quan trắc (Ví dụ: Hai Phong)
datetime	String	Mốc thời gian ghi nhận (Định dạng: 2024-09-07T15:00:00)
temp	Double	Nhiệt độ môi trường (°C)
humidity	Double	Độ ẩm không khí (%)
windspeed	Double	Tốc độ gió trung bình (km/h)
windgust	Double	Tốc độ gió giật (km/h)
sealevelpressure	Double	Áp suất khí quyển tại mực nước biển (mb)
precip	Double	Lượng mưa đo được (mm)
cloudcover	Double	Độ che phủ mây (%)
conditions	String	Mô tả tóm tắt điều kiện thời tiết
Bảng 2.2. Bảng chi tiết các trường dữ liệu
2. Schema lưu trữ Delta Lake (Output)
Dữ liệu sau khi được xử lý qua Spark Streaming [2] sẽ được lưu trữ vào Data Lakehouse [9] với các đặc tả kỹ thuật sau để đảm bảo hiệu năng truy vấn và tính nhất quán:
●	Định dạng lưu trữ (Format): Apache Parquet (định dạng cột, tối ưu cho phân tích).
●	Chiến lược phân vùng (Partitioning): Dữ liệu được phân chia thư mục theo ngày (date). Việc này giúp tăng tốc độ truy vấn khi cần lọc dữ liệu theo khoảng thời gian cụ thể.
●	Đường dẫn lưu trữ (Location): s3a://yagi-data/bronze/weather/.
2.3. Thiết kế kịch bản kiểm thử (Chaos Engineering)

Để đánh giá độ tin cậy và khả năng vận hành của hệ thống trong môi trường thực tế khắc nghiệt, nhóm thực hiện đã xây dựng các kịch bản kiểm thử dựa trên nguyên lý Chaos Engineering. Các kịch bản này tập trung vào khả năng chịu tải và khả năng tự phục hồi của hệ thống khi gặp sự cố.

Tên kịch bản	Mô tả thực hiện	Kết quả mong đợi
1. High Load (Kiểm thử chịu tải)	Giả lập tình huống bão đổ bộ mạnh bằng cách tăng tốc độ gửi message từ Producer lên gấp 10 lần bình thường (x10 speed).	Kafka phải thực hiện cơ chế đệm (buffer) dữ liệu hiệu quả mà không bị tràn bộ nhớ. Spark Streaming phải tự động mở rộng khả năng xử lý (auto-scale) để tiêu thụ hết lượng tin nhắn tồn đọng.
2. Node Failure (Giả lập sự cố phần cứng)	Thực hiện tắt nóng (force stop) container predictor (Service dự báo) trong khi hệ thống đang hoạt động để mô phỏng sự cố sập server.	Cơ chế điều phối của Docker phải phát hiện sự cố và tự động khởi động lại (auto-restart) container ngay lập tức. Quan trọng nhất là không được mất mát dữ liệu trong khoảng thời gian chết (downtime).
3. Network Partition (Giả lập mất kết nối mạng)	Cố tình ngắt kết nối mạng giữa Spark Cluster và Kafka Broker trong quá trình truyền tải dữ liệu.	Hệ thống phải có khả năng tự động kết nối lại (Reconnect) khi mạng ổn định và tiếp tục quy trình xử lý (resume processing) từ điểm bị ngắt quãng mà không gây sai lệch dữ liệu.
Bảng 2.3. Kịch bản kiểm thử 
CHƯƠNG 3. TRIỂN KHAI VÀ XÂY DỰNG

3.1. Chuẩn bị môi trường
Cấu trúc thư mục dự án:
Dự án được tổ chức theo cấu trúc tiêu chuẩn để đảm bảo sự tách biệt giữa mã nguồn xử lý, cấu hình hạ tầng và dữ liệu.
 
Hình 3.1. Cấu trúc thư mục dự án
Cấu hình file docker-compose.yaml:
Hệ thống sử dụng Docker Compose để điều phối các container. Dưới đây là cấu hình chi tiết cho các dịch vụ cốt lõi:
 
 
Hình 3.1.Cấu hình file docker-compose
Tối ưu hóa tài nguyên (16GB RAM):
Để đảm bảo hệ thống vận hành mượt mà trên hạ tầng máy tính, nhóm nghiên cứu đã áp dụng các biện pháp tối ưu sau:
●	Kafka KRaft Mode [1]: Loại bỏ hoàn toàn sự phụ thuộc vào Zookeeper, giúp tiết kiệm khoảng ~500MB RAM cho hệ thống.
●	Spark Worker [2]: Cấu hình giới hạn bộ nhớ cho mỗi Worker ở mức 2GB RAM để tránh chiếm dụng tài nguyên của các container khác.
●	Predictor Service: Sử dụng Python slim image để giảm kích thước container xuống còn khoảng ~150MB, tối ưu thời gian khởi động và dung lượng lưu trữ.

3.2. Xây dựng Ingestion Layer (Sprint 2)
File jobs/yagi_producer.py:
Đoạn mã dưới đây thực hiện chức năng đọc dữ liệu từ file CSV và gửi vào Kafka [1] topic, đóng vai trò như một trạm thu phát tín hiệu giả lập:
 
Hình 3.2. Đoạn mã yagi_producer.py

3.3. Xây dựng Processing & Storage Layer (Sprint 3)
File jobs/spark_ingestion.py:
Đoạn mã dưới đây thiết lập một Spark Streaming [2] Job để đọc dữ liệu từ Kafka [1], phân tích cú pháp (parse) JSON và ghi dữ liệu xuống Data Lake (MinIO [4]) dưới định dạng Delta Lake [3].
 
Hình 3.3. Đoạn mã spark_ingestion.py
3.4. Xây dựng MLOps Layer (Sprint 3)
Training Model trên Google Colab:
Đoạn mã dưới đây thực hiện quy trình huấn luyện mô hình phân loại (Classification) sử dụng thuật toán Random Forest để xác định mức độ nguy hiểm dựa trên các tham số khí tượng:
 
Hình 3.4.Training Model
File predictor/predictor.py:
Đây là service chạy thường trực (daemon), lắng nghe dữ liệu từ Kafka [1], sử dụng model đã huấn luyện để dự báo và gửi cảnh báo ngược lại vào Kafka topic storm-alerts:
 
Hình 3.4. Đoạn mã predictor.py

3.5. Xây dựng Serving Layer (Sprint 4)
Dashboard Streamlit: (Kế hoạch)
●	Chart 1: Tốc độ gió thực tế (Real-time line chart)
●	Chart 2: Áp suất khí quyển theo thời gian
●	Vùng cảnh báo đỏ khi gió > 60km/h

 
Hình 3.5.Dashboard Streamlit 
CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM

4.1. Kịch bản Demo: Tái hiện Bão Yagi
Quy trình Demo:
1.Khởi động hạ tầng:
 
Hình 4.1.Khởi động hạ tầng
2.Kiểm tra services:
 
Hình 4.1.Kiểm tra services
Sau khi chạy khởi động docker thì các services trong container đã chạy
3.Chạy Producer:
 
Hình 4.1.Chạy Producer
Chạy python jobs/yagi_producer.py cho thấy producer đang gửi qua kafka chờ được xử lý 
4.Quan sát Predictor:
 
Khi chạy docker logs -f yagi-predictor thì thấy nó nhận dữ liệu từ kafka được xử lý bởi spark và model đã được huấn luyện, kết quả cho thấy model AI sau khi dự đoán dựa trên các chỉ số như Wind(Gió), áp suất mực nước biển,.... từ đó cho thấy nhưng chỉ số gió trên 60km/h thì sẽ báo là DANGEROUS còn lại thì là Safe 
Kết quả hiển thị mẫu:
 
Hình 4.1.Kết quả hiển thị mẫu



Kết quả hiện trên Dashboard (Streamlit):
 





4.4. So sánh với lý thuyết

Nguyên lý	Implementation	Đánh giá
Speed Layer (Lambda)	Spark Streaming + Predictor	Real-time < 1s
Batch Layer (Lambda)	MinIO + Delta Lake	ACID, Time Travel
Serving Layer	Kafka Topics + Dashboard	Query kết hợp
Fault Tolerance	Docker restart policy	Auto-recovery
Scalability	Docker Compose	Single node only
Bảng 4.4. So sánh với lý thuyết

CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
5.1. Kết luận.
Trong khuôn khổ đồ án học phần Big Data, đề tài “Xây dựng Hệ thống Data Lakehouse & MLOps Cảnh báo Thiên tai Thời gian thực (Case Study: Tái hiện Siêu bão Yagi 2024)” đã tập trung nghiên cứu, thiết kế và triển khai một hệ thống xử lý dữ liệu lớn theo hướng hiện đại, đáp ứng các yêu cầu về xử lý thời gian thực, lưu trữ dữ liệu quy mô lớn và ứng dụng Machine Learning.
Trước hết, đề tài đã phân tích rõ tính cấp thiết của bài toán cảnh báo thiên tai trong bối cảnh biến đổi khí hậu ngày càng phức tạp, đặc biệt thông qua trường hợp siêu bão Yagi năm 2024 – một trong những cơn bão mạnh nhất trong vòng 30 năm qua tại Việt Nam. Từ đó, nhóm đã đề xuất kiến trúc hệ thống phù hợp dựa trên Lambda Architecture kết hợp Data Lakehouse, nhằm khắc phục những hạn chế của các hệ thống phân tích truyền thống.
Về mặt kỹ thuật, đề tài đã xây dựng thành công pipeline xử lý dữ liệu end-to-end, bao gồm các bước thu thập dữ liệu khí tượng, truyền tải dữ liệu dạng streaming, xử lý thời gian thực, lưu trữ dữ liệu và hiển thị kết quả phân tích. Việc sử dụng Apache Kafka [1] và Apache Spark Structured Streaming [2] giúp hệ thống đạt được khả năng xử lý dữ liệu với độ trễ thấp, đáp ứng yêu cầu cảnh báo sớm.
Bên cạnh đó, kiến trúc Data Lakehouse [9] dựa trên MinIO [4] và Delta Lake [3] đã được triển khai hiệu quả, cho phép lưu trữ dữ liệu khí tượng ở dạng thô nhưng vẫn đảm bảo các đặc tính quan trọng như tính nhất quán, kiểm soát schema và truy vết dữ liệu theo thời gian. Đây là nền tảng quan trọng để phục vụ các tác vụ phân tích và huấn luyện mô hình Machine Learning.
Ngoài xử lý dữ liệu, đề tài cũng đã bước đầu ứng dụng Machine Learning và MLOps trong hệ thống nhằm đánh giá mức độ nguy hiểm của bão dựa trên các chỉ số khí tượng. Việc tích hợp quy trình MLOps giúp tự động hóa quá trình huấn luyện và triển khai mô hình, góp phần nâng cao tính thông minh và khả năng mở rộng của hệ thống.
5.2. Hạn chế của đề tài.
Mặc dù đã đạt được các mục tiêu nghiên cứu đề ra, đề tài vẫn còn tồn tại một số hạn chế nhất định:
●	Dữ liệu sử dụng trong hệ thống được thu thập từ Visual Crossing Weather dưới dạng dữ liệu lịch sử, sau đó được mô phỏng lại thành luồng dữ liệu streaming. Điều này chưa phản ánh đầy đủ điều kiện vận hành của một hệ thống cảnh báo thiên tai sử dụng dữ liệu cảm biến thời gian thực ngoài thực tế.
Nguồn tham khảo: https://www.visualcrossing.com/weather-query-builder/

●	Hệ thống được triển khai trên môi trường Docker đơn node, do đó chưa đánh giá được đầy đủ khả năng mở rộng, chịu tải và hiệu năng của hệ thống trong môi trường cluster thực tế.
●	Mô hình Machine Learning được sử dụng ở mức cơ bản, chủ yếu nhằm minh họa quy trình MLOps và cơ chế cảnh báo, chưa tập trung tối ưu độ chính xác của dự báo.
●	Cơ chế cảnh báo trong hệ thống mang tính mô phỏng, chưa được tích hợp với các kênh cảnh báo thực tế như SMS, ứng dụng di động hoặc hệ thống điều hành khẩn cấp.
5.3. Hướng phát triển trong tương lai.
Từ những kết quả đạt được và các hạn chế còn tồn tại, đề tài có thể được mở rộng và phát triển theo các hướng sau:
5.3.1. Tích hợp dữ liệu thời gian thực từ các nguồn thực tế
Trong tương lai, hệ thống có thể được tích hợp trực tiếp với:
●	Các cảm biến IoT khí tượng
●	Dữ liệu radar thời tiết
●	Dữ liệu vệ tinh
Việc này sẽ giúp hệ thống vận hành trong môi trường thực tế, nâng cao độ chính xác và tính kịp thời của các cảnh báo.
5.3.2. Triển khai hệ thống trên môi trường phân tán
Hệ thống có thể được triển khai trên các nền tảng:
●	Kafka Cluster
●	Spark Cluster
●	Kubernetes
Nhằm đánh giá khả năng mở rộng, cân bằng tải và tự phục hồi của hệ thống khi xử lý dữ liệu lớn trong điều kiện khắc nghiệt.
5.3.3. Nâng cao mô hình Machine Learning và MLOps.
Các hướng phát triển tiếp theo bao gồm:
●	Áp dụng các mô hình dự báo nâng cao như LSTM, GRU hoặc Transformer.
●	Theo dõi hiệu năng mô hình theo thời gian và phát hiện hiện tượng drift dữ liệu
●	Tự động hóa toàn bộ vòng đời mô hình theo hướng MLOps hoàn chỉnh
5.3.4. Mở rộng phạm vi ứng dụng.
Ngoài bài toán cảnh báo bão, kiến trúc và hệ thống trong đề tài có thể được mở rộng để ứng dụng trong các lĩnh vực khác như:
●	Cảnh báo lũ lụt và sạt lở đất
●	Giám sát môi trường và biến đổi khí hậu
●	Phát hiện sự cố hạ tầng và các hệ thống giám sát thời gian thực khác

 
TÀI LIỆU THAM KHẢO

Tài liệu tham khảo: 
[1]	Apache Kafka Documentation - Truy cập từ https://kafka.apache.org/documentation/ 
[2]	Apache Spark Documentation - Truy cập từ https://spark.apache.org/docs/latest/
[3]	Delta Lake Documentation - Truy cập từ https://docs.delta.io/latest/
[4]	MinIO Documentation - Truy cập từ https://docs.min.io/
[5]	Visual Crossing Weather Data - Truy cập từ https://www.visualcrossing.com/
[6]	Marz, Nathan & Warren, James. (2015). Big Data: Principles and best practices of scalable real-time data systems. Manning Publications.
[7]	Kleppmann, Martin. (2017). Designing Data-Intensive Applications. O'Reilly Media.
[8]	Lambda Architecture - Truy cập từ http://lambda-architecture.net/
[9]	Armbrust, M., et al. (2021). Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics. CIDR 2021. [PDF] https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf
[10]	Weather Prediction Model using Random Forest Algorithm and Apache Spark. International Journal of Trend in Scientific Research and Development (IJTSRD). [PDF] https://www.ijtsrd.com/papers/ijtsrd23706.pdf
[11]	Dimovski, A., et al. (2015). Lambda Architecture for Real Time Big Data Analytic. ICT Innovations 2015. [PDF] https://ictinnovations.org/2015/papers/ICT-Innovations-2015-Lambda-Architecture.pdf
[12]	Strategies for Big Data Analytics through Lambda Architectures in Volatile Environments. arXiv:2101.05765. [PDF] https://arxiv.org/pdf/2101.05765.pdf
[13]	Bão Yagi (2024) - Wikipedia Tiếng Việt. Truy cập từ https://vi.wikipedia.org/wiki/Bão_Yagi_(2024)
[14]	Báo Tiền Phong (2024). Bão Yagi mạnh lên thành siêu bão. Truy cập từ https://tienphong.vn/bao-yagi-manh-len-thanh-sieu-bao-trong-hom-nay-post1669853.tpo
[15]	Streamlit Documentation - Truy cập từ https://docs.streamlit.io/
[16]	Docker Documentation - Truy cập từ https://docs.docker.com/
[17]	Docker Compose Documentation - Truy cập từ https://docs.docker.com/compose/
[18]	Scikit-learn Documentation - Truy cập từ https://scikit-learn.org/stable/documentation.html
[19]	Python Official Documentation - Truy cập từ https://docs.python.org/3/
[20]	Portainer Documentation - Truy cập từ https://docs.portainer.io/
[21]	Pandas Documentation - Truy cập từ https://pandas.pydata.org/docs/
[22]	Random Forest Algorithm - Scikit-learn. Truy cập từ https://scikit-learn.org/stable/modules/ensemble.html#random-forests
[23]	Apache Parquet Documentation - Truy cập từ https://parquet.apache.org/docs/
[24]	ERPS Vietnam (2023). 3V Big Data là gì? Truy cập từ https://erps.vn/3v-big-data-la-gi/
[25]	Viblo Asia. Batch Processing và Stream Processing. Truy cập từ https://viblo.asia/p/batch-processing-va-stream-processing-kham-pha-hai-phuong-phap-xu-ly-du-lieu-chu-luc-gwd43zXrVX9
[26]	V4C AI Blog. Implementing Delta Lake Time Travel. Truy cập từ https://www.v4c.ai/blog/implementing-delta-lake-time-travel
