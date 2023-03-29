@pytest.mark.skip: Testin geçici olarak devre dışı bırakmak istediğinizde veya belirtilen testi atlamak için kullanılır.

@pytest.mark.xfail: İlgili testin başarısız olması beklenir, ancak bu başarısızlık, diğer testlerin çalışmasını durdurmaz.

@pytest.mark.timeout: Testin belirtilen süre içinde tamamlanması gereken testleri işaretlemek için kullanılır. Süre aşılırsa, test başarısız olur.

@pytest.fixture: Belirli bir kapsamda kullanılabilen önceden hazırlanmış verileri veya objeleri sağlar. Bu kapsam, session, module, class ve function olabilir.

@pytest.mark.order: Testlerin sırasını belirlemek için kullanılır.

@pytest.mark.dependency: Testler arasındaki bağımlılıkları belirlemek için kullanılır. Bu şekilde, bir testin öncesinde veya sonrasında belirli bir testin çalıştırılması sağlanabilir.

@pytest.mark.slow: Belirli bir testin uzun süre çalışacağı veya yavaş çalışacağı durumlarda kullanılır. Bu şekilde, test süresinin uzunluğuna dikkat çekilerek, test senaryosunun optimize edilmesi sağlanabilir.
